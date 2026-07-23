import MaterialCard from './MaterialCard'

export default function TopologyDisplay({ topology, count, onMaterialClick }) {
  return (
    <div className="topology-container">
      <h3>材料拓扑 (共需 {count} 个)</h3>
      <div className="topology-layers">
        {Object.entries(topology)
          .sort(([a], [b]) => Number(a) - Number(b))
          .map(([layer, items]) => (
            <div key={layer} className={`layer layer-${layer}`}>
              <div className="layer-title">第 {layer} 层</div>
              <div className="layer-items">
                {items.map((mat, idx) => (
                  <MaterialCard key={idx} mat={mat} onClick={onMaterialClick} />
                ))}
              </div>
            </div>
          ))}
      </div>
    </div>
  )
}