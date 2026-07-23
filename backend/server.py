import importlib
import inspect
import json
import logging
import pkgutil
import threading
import time
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from backend.materials import materials

# ── Logging ──────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(threadName)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("server.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger("archerage")

# ── Connection counter (thread-safe) ─────────────────────────────────
_active_connections = 0
_conn_lock = threading.Lock()
_total_requests = 0


def _inc_connections():
    global _active_connections, _total_requests
    with _conn_lock:
        _active_connections += 1
        _total_requests += 1


def _dec_connections():
    global _active_connections
    with _conn_lock:
        _active_connections -= 1


def get_connection_count():
    """Return (active_connections, total_requests)."""
    with _conn_lock:
        return _active_connections, _total_requests


# ── Material discovery ───────────────────────────────────────────────
def _discover_material_classes():
    registry = {}
    package = importlib.import_module("backend.materials")
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"backend.materials.{module_name}")
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__ != module.__name__:
                continue
            if cls is materials.Meterial or cls is materials.Template:
                continue
            if not issubclass(cls, materials.Meterial):
                continue
            try:
                instance = cls()
            except Exception:
                continue
            registry[instance.id] = cls
    return registry


MATERIAL_CLASS_REGISTRY = _discover_material_classes()

MATERIAL_CATEGORY_MAP = {
    item_id: cls.__module__.rsplit(".", 1)[-1]
    for item_id, cls in MATERIAL_CLASS_REGISTRY.items()
}


def get_material_category(item_id: int) -> str:
    return MATERIAL_CATEGORY_MAP.get(int(item_id), "unknown")


def get_material_by_id(item_id: int):
    cls = MATERIAL_CLASS_REGISTRY.get(int(item_id))
    if cls is None:
        raise KeyError(f"Unknown item id: {item_id}")
    return cls()


def topology_to_dict(topology: dict):
    result = {}
    for layer, items in sorted(topology.items(), key=lambda item: int(item[0])):
        layer_items = []
        for material, count in sorted(
            items.items(), key=lambda entry: (entry[0].id, entry[0].__class__.__name__)
        ):
            layer_items.append({
                "item_id": material.id,
                "name": materials.GetItemNameFromId(material.id, True),
                "ch_name": materials.GetItemNameFromId(material.id, False),
                "category": get_material_category(material.id),
                "count": count,
            })
        result[str(layer)] = layer_items
    return result


# ── Request handler ──────────────────────────────────────────────────
class TopologyRequestHandler(BaseHTTPRequestHandler):
    """
    Thread-per-request handler.  Each handler instance lives for the
    duration of one HTTP request — we treat its lifetime as one active
    connection.
    """

    def do_GET(self):
        _inc_connections()
        t_start = time.time()
        try:
            self._handle_get()
        finally:
            elapsed = (time.time() - t_start) * 1000
            client_ip = self.client_address[0]
            logger.info(
                "%s %s → %d (%.1f ms)",
                self.command,
                self.path,
                self._last_status if hasattr(self, "_last_status") else 0,
                elapsed,
            )
            _dec_connections()

    def _handle_get(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path == "/list_items":
            self._send_json(HTTPStatus.OK, self._list_items())
            return

        if path == "/query_items":
            self._queryItems(params)
            return

        if path == "/stats":
            active, total = get_connection_count()
            self._send_json(
                HTTPStatus.OK,
                {
                    "active_connections": active,
                    "total_requests": total,
                },
            )
            return

        self._send_json(HTTPStatus.NOT_FOUND, {})

    def _queryItems(self, params):
        item_id = params.get("item_id", [None])[0]
        cnt = params.get("cnt", [1])[0]
        if item_id is None:
            self._send_json(
                HTTPStatus.BAD_REQUEST,
                {"error": "Missing required query parameter: item_id"},
            )
            return

        try:
            item = get_material_by_id(int(item_id))
            topology = item.TopologyV3(int(cnt))
            payload = {
                "item_id": item.id,
                "topology": topology_to_dict(topology),
            }
            self._send_json(HTTPStatus.OK, payload)
        except ValueError:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "item_id must be an integer"})
        except KeyError as exc:
            self._send_json(HTTPStatus.NOT_FOUND, {"error": str(exc)})
        except Exception as exc:  # pragma: no cover
            logger.exception("Unhandled error in _queryItems")
            self._send_json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})

    def _list_items(self):
        items = []
        for item_id, cls in sorted(MATERIAL_CLASS_REGISTRY.items(), key=lambda entry: entry[0]):
            instance = cls()
            items.append({
                "item_id": instance.id,
                "name": materials.GetItemNameFromId(instance.id, True),
                "ch_name": materials.GetItemNameFromId(instance.id, False),
                "category": get_material_category(instance.id),
            })
        return items

    def _send_json(self, status_code: int, payload: dict):
        self._last_status = status_code
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # Keep the server's own log quiet (we handle logging ourselves)
    def log_message(self, format, *args):
        return


# ── Server lifecycle ─────────────────────────────────────────────────
def run_server(host: str = "127.0.0.1", port: int = 8000, blocking: bool = True):
    httpd = ThreadingHTTPServer((host, port), TopologyRequestHandler)
    logger.info("服务器启动 %s:%d", host, port)
    thread = None
    if blocking:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("收到中断信号，正在关闭服务器...")
            httpd.shutdown()
    else:
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
    return httpd, thread


def stop_server(httpd):
    logger.info("服务器已停止")
    httpd.shutdown()
    httpd.server_close()


if __name__ == "__main__":
    run_server()