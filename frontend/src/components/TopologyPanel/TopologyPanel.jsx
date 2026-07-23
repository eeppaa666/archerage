import QueryBar from './QueryBar'
import TopologyDisplay from './TopologyDisplay'

export default function TopologyPanel({
  selectedItem,
  topology,
  error,
  loading,
  historyIndex,
  historyStackLength,
  canGoBack,
  canGoForward,
  onGoBack,
  onGoForward,
  count,
  onCountChange,
  onQuery,
  onMaterialClick,
}) {
  if (!selectedItem) {
    return (
      <section className="content">
        <div className="placeholder">
          👈 从左侧列表中选择一个物品
        </div>
      </section>
    )
  }

  return (
    <section className="content">
      <QueryBar
        selectedItem={selectedItem}
        historyIndex={historyIndex}
        historyStackLength={historyStackLength}
        canGoBack={canGoBack}
        canGoForward={canGoForward}
        onGoBack={onGoBack}
        onGoForward={onGoForward}
        count={count}
        onCountChange={onCountChange}
        loading={loading}
        onQuery={onQuery}
      />

      {error && <div className="error">{error}</div>}

      {topology && (
        <TopologyDisplay
          topology={topology}
          count={count}
          onMaterialClick={onMaterialClick}
        />
      )}

      {!topology && !loading && !error && (
        <div className="placeholder">
          点击「查询材料」查看制作 {selectedItem.ch_name} 所需的材料拓扑
        </div>
      )}
    </section>
  )
}