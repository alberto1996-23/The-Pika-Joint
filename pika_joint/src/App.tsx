import { useState } from 'react'
import './App.css'
import Header from './components/header'
import MenuCategory from './components/MenuCategory'
import OrderPanel from './components/OrderPanel'
import { menuItems, type MenuItem } from './data/MenuData'

type OrderItem = {
  name: string
  price: string
  quantity: number
}

function App() {
  const [orderItems, setOrderItems] = useState<OrderItem[]>([])

  const breakfastItems = menuItems.filter((item) => item.category === 'Breakfast')
  const lunchItems = menuItems.filter((item) => item.category === 'Lunch')
  const dinnerItems = menuItems.filter((item) => item.category === 'Dinner')
  const dessertItems = menuItems.filter((item) => item.category === 'Dessert')

  function handleAddToOrder(item: MenuItem) {
    setOrderItems((prevItems) => {
      const existingItem = prevItems.find((orderItem) => orderItem.name === item.name)

      if (existingItem) {
        return prevItems.map((orderItem) =>
          orderItem.name === item.name
            ? { ...orderItem, quantity: orderItem.quantity + 1 }
            : orderItem
        )
      }

      return [...prevItems, { name: item.name, price: item.price, quantity: 1 }]
    })
  }

  function handleIncrease(name: string) {
    setOrderItems((prevItems) =>
      prevItems.map((item) =>
        item.name === name ? { ...item, quantity: item.quantity + 1 } : item
      )
    )
  }

  function handleDecrease(name: string) {
    setOrderItems((prevItems) =>
      prevItems
        .map((item) =>
          item.name === name ? { ...item, quantity: item.quantity - 1 } : item
        )
        .filter((item) => item.quantity > 0)
    )
  }

  return (
    <div className="app-container">
      <Header />

      <div className="content-layout">
        <main>
          <MenuCategory title="Breakfast" items={breakfastItems} onAddToOrder={handleAddToOrder} />
          <MenuCategory title="Lunch" items={lunchItems} onAddToOrder={handleAddToOrder} />
          <MenuCategory title="Dinner" items={dinnerItems} onAddToOrder={handleAddToOrder} />
          <MenuCategory title="Dessert" items={dessertItems} onAddToOrder={handleAddToOrder} />
        </main>

        <OrderPanel
          orderItems={orderItems}
          onIncrease={handleIncrease}
          onDecrease={handleDecrease}
        />
      </div>
    </div>
  )
}

export default App
