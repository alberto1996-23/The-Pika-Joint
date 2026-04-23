export type MenuItem = {
  name: string
  description: string
  category: string
  price: string
}

export const menuItems: MenuItem[] = [
  {
    name: 'Exeggcute Sandwich',
    description: 'A muffin sandwich with 2 eggs, sausage, and cheese.',
    category: 'Breakfast',
    price: '$3.00',
  },
  {
    name: 'Cherubi Pancakes',
    description: '4 pancakes topped with whipped cream, blueberries, and cherries.',
    category: 'Breakfast',
    price: '$4.00',
  },
  {
    name: 'Pika Patty',
    description: 'A Pikachu-themed burger with patties, cheese, onions, lettuce, tomatoes, and condiments.',
    category: 'Lunch',
    price: '$5.00',
  },
  {
    name: 'Farfetch’d Leek Salad',
    description: 'A salad with cucumbers, chopped leek, and choice of fruits and veggies.',
    category: 'Lunch',
    price: '$4.00',
  },
  {
    name: 'Fried Magikarp Strips',
    description: 'Fish strips served with chips and a drink choice.',
    category: 'Lunch',
    price: '$7.50',
  },
  {
    name: 'Krabby Legs',
    description: 'Crab legs served with butter and lemon.',
    category: 'Dinner',
    price: '$6.00 - $12.00',
  },
  {
    name: 'Combusken Pesto Pasta',
    description: 'Penne with pesto and chicken breast.',
    category: 'Dinner',
    price: '$8.00',
  },
  {
    name: 'Peking Psyduck',
    description: 'Chopped Psyduck with soy sauce and honey, served with ranch.',
    category: 'Dinner',
    price: '$9.00',
  },
  {
    name: 'Vanilluxe Ice Cream',
    description: 'Vanilla ice cream served with sprinkles and whipped cream.',
    category: 'Dessert',
    price: '$2.50',
  },
  {
    name: 'Appletun Turnover',
    description: 'Apple turnover.',
    category: 'Dessert',
    price: '$3.00',
  },
  {
    name: 'Alcremie Cake',
    description: 'Vanilla or chocolate cake with whipped creme and a cherry on top.',
    category: 'Dessert',
    price: '$6.00',
  },
]