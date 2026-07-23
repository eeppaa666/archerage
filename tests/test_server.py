import json
import threading
import unittest
from urllib.request import Request, urlopen

from backend.materials.ingot import SturdyIngot
from backend import server


class TopologyServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd, cls.thread = server.run_server(host="127.0.0.1", port=0, blocking=False)
        cls.base_url = f"http://127.0.0.1:{cls.httpd.server_address[1]}"

    @classmethod
    def tearDownClass(cls):
        server.stop_server(cls.httpd)
        cls.thread.join(timeout=2)

    def test_query_items_endpoint_returns_json(self):
        item = SturdyIngot()
        request = Request(
            f"{self.base_url}/query_items?item_id={item.id}",
            headers={"Accept": "application/json"},
        )

        with urlopen(request, timeout=5) as response:
            self.assertEqual(response.status, 200)
            payload = json.load(response)

        self.assertEqual(payload["item_id"], item.id)
        self.assertIn("topology", payload)
        self.assertTrue(isinstance(payload["topology"], dict))
        self.assertTrue(payload["topology"])

    def test_list_items_endpoint_lists_all_items(self):
        request = Request(
            f"{self.base_url}/list_items",
            headers={"Accept": "application/json"},
        )

        with urlopen(request, timeout=5) as response:
            self.assertEqual(response.status, 200)
            payload = json.load(response)

        self.assertTrue(isinstance(payload, list))
        self.assertTrue(payload)
        first_item = payload[0]
        self.assertIn("item_id", first_item)
        self.assertIn("name", first_item)
        self.assertIn("ch_name", first_item)

    def test_stats_endpoint_returns_connection_info(self):
        request = Request(
            f"{self.base_url}/stats",
            headers={"Accept": "application/json"},
        )

        with urlopen(request, timeout=5) as response:
            self.assertEqual(response.status, 200)
            payload = json.load(response)

        self.assertIn("active_connections", payload)
        self.assertIn("total_requests", payload)
        self.assertTrue(isinstance(payload["active_connections"], int))
        self.assertTrue(isinstance(payload["total_requests"], int))
        # Should have at least tracked this request itself
        self.assertGreaterEqual(payload["total_requests"], 1)


if __name__ == "__main__":
    unittest.main()