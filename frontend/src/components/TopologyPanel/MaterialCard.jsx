export default function MaterialCard({ mat, onClick }) {
  return (
    <div
      className="material-card clickable"
      onClick={() => onClick(mat.item_id)}
      title={`查看 [${mat.item_id}] ${mat.ch_name} 的材料拓扑`}
    >
      <div className="mat-name">{mat.ch_name}</div>
      <div className="mat-eng">{mat.name || "\u00A0"}</div>
      <div className="mat-category">{mat.category}</div>
      <div className="mat-id">ID: {mat.item_id}</div>
      <div className="mat-count">×{mat.count}</div>
    </div>
  )
}