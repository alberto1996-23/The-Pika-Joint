import MenuItemCard from './MenuItemCard'
import type { MenuItem } from '../data/MenuData'

type MenuCategoryProps = {
  title: string
  items: MenuItem[]
}

function MenuCategory({ title, items }: MenuCategoryProps) {
  return (
    <section className="menu-category">
      <h2>{title}</h2>
      <div className="menu-grid">
        {items.map((item) => (
          <MenuItemCard
            key={item.name}
            name={item.name}
            description={item.description}
            price={item.price}
          />
        ))}
      </div>
    </section>
  )
}

export default MenuCategory