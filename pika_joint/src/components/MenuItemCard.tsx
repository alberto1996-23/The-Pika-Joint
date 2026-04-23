type MenuItemCardProps = {
  name: string
  description: string
  price: string
  onAddToOrder: () => void
}

function MenuItemCard({ name, description, price, onAddToOrder }: MenuItemCardProps) {
  return (
    <div className="menu-item-card">
      <h3>{name}</h3>
      <p>{description}</p>
      <span>{price}</span>
      <br />
      <button onClick={onAddToOrder}>Add to Order</button>
    </div>
  )
}

export default MenuItemCard