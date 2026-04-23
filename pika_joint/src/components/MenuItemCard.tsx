type MenuItemCardProps = {
  name: string
  description: string
  price: string
}

function MenuItemCard({ name, description, price }: MenuItemCardProps) {
  return (
    <div className="menu-item-card">
      <h3>{name}</h3>
      <p>{description}</p>
      <span>{price}</span>
    </div>
  )
}

export default MenuItemCard