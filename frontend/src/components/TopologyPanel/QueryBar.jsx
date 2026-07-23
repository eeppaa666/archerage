import './TopologyPanel.css'

export default function QueryBar({
  selectedItem,
  historyIndex,
  historyStackLength,
  canGoBack,
  canGoForward,
  onGoBack,
  onGoForward,
  count,
  onCountChange,
  loading,
  onQuery,
}) {
  return (
    <div className="query-bar">
      <h2>
        选中: <span className="selected-name">[{selectedItem.item_id}] {selectedItem.ch_name}</span>
        <span className="selected-category">{selectedItem.category}</span>
      </h2>
      <div className="query-controls">
        <div className="history-nav">
          <button
            className="nav-btn"
            onClick={onGoBack}
            disabled={!canGoBack}
            title="上一个查看的物品"
          >
            ◀
          </button>
          <span className="nav-info">
            {historyIndex + 1} / {historyStackLength}
          </span>
          <button
            className="nav-btn"
            onClick={onGoForward}
            disabled={!canGoForward}
            title="下一个查看的物品"
          >
            ▶
          </button>
        </div>
        <label>
          数量:
          <input
            type="number"
            min="1"
            value={count}
            onChange={e => onCountChange(Math.max(1, parseInt(e.target.value) || 1))}
          />
        </label>
        <button onClick={onQuery} disabled={loading}>
          {loading ? '查询中...' : '查询材料'}
        </button>
      </div>
    </div>
  )
}