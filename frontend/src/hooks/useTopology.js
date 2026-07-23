import { useState, useCallback, useRef, useEffect } from 'react'
import { API_BASE } from '../config'

export function useTopology() {
  const [selectedId, setSelectedId] = useState(null)
  const [topology, setTopology] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [count, setCount] = useState(1)
  const countRef = useRef(count)
  const selectedIdRef = useRef(null)
  const topologyCache = useRef({}) // { [itemId]: topologyData }

  // Keep countRef in sync
  useEffect(() => {
    countRef.current = count
  }, [count])

  const doQuery = useCallback((itemId, forceRefresh = false) => {
    if (!itemId) return
    setLoading(true)
    setError(null)
    setTopology(null)

    const curCnt = countRef.current
    const cacheKey = `${itemId}:${curCnt}`

    // Check cache first (skip if forced refresh)
    if (!forceRefresh && topologyCache.current[cacheKey]) {
      setTopology(topologyCache.current[cacheKey])
      setLoading(false)
      return
    }

    const params = new URLSearchParams({ item_id: itemId, cnt: curCnt })
    fetch(`${API_BASE}/query_items?${params}`)
      .then(res => {
        if (!res.ok) return res.json().then(e => { throw new Error(e.error) })
        return res.json()
      })
      .then(data => {
        const topo = data.topology
        topologyCache.current[cacheKey] = topo
        setTopology(topo)
      })
      .catch(err => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  const selectItem = useCallback((itemId) => {
    selectedIdRef.current = itemId
    setSelectedId(itemId)
    doQuery(itemId)
  }, [doQuery])

  const refreshQuery = useCallback(() => {
    doQuery(selectedId, true)
  }, [doQuery, selectedId])

  return {
    selectedId,
    selectedIdRef,
    topology,
    loading,
    error,
    count,
    setCount,
    selectItem,
    refreshQuery,
  }
}