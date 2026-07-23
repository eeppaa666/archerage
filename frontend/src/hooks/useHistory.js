import { useState, useCallback, useRef, useEffect } from 'react'

export function useHistory() {
  const [historyStack, setHistoryStack] = useState([])
  const [historyIndex, setHistoryIndex] = useState(-1)
  const historyIndexRef = useRef(-1)

  // Sync ref
  useEffect(() => {
    historyIndexRef.current = historyIndex
  }, [historyIndex])

  // Push a new item to history (append mode)
  const pushHistory = useCallback((itemId) => {
    const curIdx = historyIndexRef.current
    setHistoryStack(prev => {
      const newStack = prev.slice(0, curIdx + 1)
      if (newStack[newStack.length - 1] !== itemId) {
        newStack.push(itemId)
      }
      return newStack
    })
    setHistoryIndex(prev => prev + 1)
  }, [])

  // Reset history to a single item
  const resetHistory = useCallback((itemId) => {
    setHistoryStack([itemId])
    setHistoryIndex(0)
  }, [])

  // Navigate: just move index, no history change
  const canGoBack = historyIndex > 0
  const canGoForward = historyIndex < historyStack.length - 1

  const getBackItemId = useCallback(() => {
    if (!canGoBack) return null
    return historyStack[historyIndex - 1]
  }, [canGoBack, historyIndex, historyStack])

  const getForwardItemId = useCallback(() => {
    if (!canGoForward) return null
    return historyStack[historyIndex + 1]
  }, [canGoForward, historyIndex, historyStack])

  return {
    historyStack,
    historyIndex,
    pushHistory,
    resetHistory,
    setHistoryIndex,
    canGoBack,
    canGoForward,
    getBackItemId,
    getForwardItemId,
  }
}