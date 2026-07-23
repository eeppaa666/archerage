import { useRef, useEffect } from 'react'
import './Sidebar.css'

export default function Sidebar({
  sortedCategories,
  groupedItems,
  collapsedCategories,
  toggleCategory,
  selectedId,
  error,
  onItemSelect,
}) {
  const sidebarRef = useRef(null)

  // Scroll to selected item in sidebar when selectedId changes
  useEffect(() => {
    if (selectedId && sidebarRef.current) {
      const el = sidebarRef.current.querySelector(`[data-item-id="${selectedId}"]`)
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'nearest' })
      }
    }
  }, [selectedId])

  return (
    <aside className="sidebar" ref={sidebarRef}>
      <h2>物品列表</h2>
      {error && (
        <div className="error">{error}</div>
      )}
      <div className="item-list">
        {sortedCategories.map(cat => (
          <div key={cat} className="category-group">
            <div
              className="category-header"
              onClick={() => toggleCategory(cat)}
            >
              <span className={`category-arrow ${collapsedCategories[cat] ? 'collapsed' : ''}`}>▼</span>
              <span className="category-name">{cat}</span>
              <span className="category-count">{groupedItems[cat].length}</span>
            </div>
            <ul className={`category-items ${collapsedCategories[cat] ? 'hidden' : ''}`}>
              {groupedItems[cat].map(item => (
                <li
                  key={item.item_id}
                  data-item-id={item.item_id}
                  className={`item-row ${selectedId === item.item_id ? 'selected' : ''}`}
                  onClick={() => onItemSelect(item.item_id, 'reset')}
                >
                  <span className="item-id">[{item.item_id}]</span>
                  <div className="item-info">
                    <span className="item-name">{item.ch_name}</span>
                    <span className="item-eng">{item.name}</span>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </aside>
  )
}