import './App.css'
import Header from './components/header'
import MenuCategory from './components/MenuCategory'
import { menuItems } from './data/MenuData'

function App() {
  const breakfastItems = menuItems.filter((item) => item.category === 'Breakfast')
  const lunchItems = menuItems.filter((item) => item.category === 'Lunch')
  const dinnerItems = menuItems.filter((item) => item.category === 'Dinner')
  const dessertItems = menuItems.filter((item) => item.category === 'Dessert')

  return (
    <div className="app-container">
      <Header />

      <main>
        <MenuCategory title="Breakfast" items={breakfastItems} />
        <MenuCategory title="Lunch" items={lunchItems} />
        <MenuCategory title="Dinner" items={dinnerItems} />
        <MenuCategory title="Dessert" items={dessertItems} />
      </main>
    </div>
  )
}

export default App
