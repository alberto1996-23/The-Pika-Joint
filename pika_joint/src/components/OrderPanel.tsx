type OrderItem = {
  name: string
  price: string
  quantity: number
}

type OrderPanelProps = {
  orderItems: OrderItem[]
  onIncrease: (name: string) => void
  onDecrease: (name: string) => void
}

function OrderPanel({ orderItems, onIncrease, onDecrease }: OrderPanelProps) {
  return (
    <aside className="order-panel">
      <h2>Your Order</h2>

      {orderItems.length === 0 ? (
        <p>No items added yet.</p>
      ) : (
        orderItems.map((item) => (
          <div key={item.name} className="order-item">
            <h3>{item.name}</h3>
            <p>{item.price}</p>
            <div className="quantity-controls">
              <button onClick={() => onDecrease(item.name)}>-</button>
              <span>{item.quantity}</span>
              <button onClick={() => onIncrease(item.name)}>+</button>
            </div>
          </div>
        ))
      )}
    </aside>
  )
}

export default OrderPanel