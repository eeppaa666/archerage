import { useCallback } from 'react'
import './App.css'
import Sidebar from './components/Sidebar/Sidebar'
import TopologyPanel from './components/TopologyPanel/TopologyPanel'
import { useItems } from './hooks/useItems'
import { useTopology } from './hooks/useTopology'
import { useHistory } from './hooks/useHistory'

function App() {
  const {
    items,
    groupedItems,
    sortedCategories,
    collapsedCategories,
    toggleCategory,
    setCollapsedCategories,
    error: itemError,
  } = useItems()

  const {
    selectedId,
    selectedIdRef,
    topology,
    loading,
    error: topoError,
    count,
    setCount,
    selectItem,
    refreshQuery,
  } = useTopology()

  const {
    historyIndex,
    historyStack,
    pushHistory,
    resetHistory,
    setHistoryIndex,
    canGoBack,
    canGoForward,
    getBackItemId,
    getForwardItemId,
  } = useHistory()

  // Select an item with appropriate history mode
  // historyMode: 'push' = from topology card, 'reset' = from sidebar, 'nav' = forward/back
  const handleItemSelect = useCallback((itemId, historyMode = 'push') => {
    // If clicking the same item from topology, skip entirely
    if (historyMode === 'push' && itemId === selectedIdRef.current) return

    // Expand the category if collapsed
    const targetItem = items.find(i => i.item_id === itemId)
    if (targetItem) {
      setCollapsedCategories(prev => {
        if (prev[targetItem.category]) {
          return { ...prev, [targetItem.category]: false }
        }
        return prev
      })
    }

    selectItem(itemId)

    if (historyMode === 'push') {
      pushHistory(itemId)
    } else if (historyMode === 'reset') {
      resetHistory(itemId)
    }
    // 'nav' mode: no history change
  }, [items, selectItem, selectedIdRef, pushHistory, resetHistory, setCollapsedCategories])

  const goBack = useCallback(() => {
    const prevItemId = getBackItemId()
    if (prevItemId != null) {
      setHistoryIndex(historyIndex - 1)
      handleItemSelect(prevItemId, 'nav')
    }
  }, [getBackItemId, historyIndex, setHistoryIndex, handleItemSelect])

  const goForward = useCallback(() => {
    const nextItemId = getForwardItemId()
    if (nextItemId != null) {
      setHistoryIndex(historyIndex + 1)
      handleItemSelect(nextItemId, 'nav')
    }
  }, [getForwardItemId, historyIndex, setHistoryIndex, handleItemSelect])

  const handleMaterialClick = useCallback((itemId) => {
    handleItemSelect(itemId, 'push')
  }, [handleItemSelect])

  const displayError = itemError || topoError
  const selectedItem = items.find(i => i.item_id === selectedId)

  return (
    <div className="app">
      <header className="header">
        <h1>📦 物品材料拓扑查询</h1>
      </header>

      <div className="main">
        <Sidebar
          sortedCategories={sortedCategories}
          groupedItems={groupedItems}
          collapsedCategories={collapsedCategories}
          toggleCategory={toggleCategory}
          selectedId={selectedId}
          error={displayError && !topology ? displayError : null}
          onItemSelect={handleItemSelect}
        />

        <TopologyPanel
          selectedItem={selectedItem}
          topology={topology}
          error={topoError}
          loading={loading}
          historyIndex={historyIndex}
          historyStackLength={historyStack.length}
          canGoBack={canGoBack}
          canGoForward={canGoForward}
          onGoBack={goBack}
          onGoForward={goForward}
          count={count}
          onCountChange={setCount}
          onQuery={refreshQuery}
          onMaterialClick={handleMaterialClick}
        />
      </div>
    </div>
  )
}

export default App