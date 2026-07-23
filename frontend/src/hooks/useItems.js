import { useState, useEffect } from 'react'
import { API_BASE } from '../config'

export function useItems() {
  const [items, setItems] = useState([])
  const [collapsedCategories, setCollapsedCategories] = useState({})
  const [error, setError] = useState(null)

  // Load item list on mount
  useEffect(() => {
    fetch(`${API_BASE}/list_items`)
      .then(res => res.json())
      .then(data => setItems(data))
      .catch(err => setError('加载物品列表失败: ' + err.message))
  }, [])

  // Group items by category
  const groupedItems = items.reduce((acc, item) => {
    const cat = item.category || 'unknown'
    if (!acc[cat]) acc[cat] = []
    acc[cat].push(item)
    return acc
  }, {})

  // Sort categories alphabetically
  const sortedCategories = Object.keys(groupedItems).sort()

  // Toggle category collapse
  const toggleCategory = (cat) => {
    setCollapsedCategories(prev => ({ ...prev, [cat]: !prev[cat] }))
  }

  return {
    items,
    groupedItems,
    sortedCategories,
    collapsedCategories,
    toggleCategory,
    setCollapsedCategories,
    error,
  }
}