type OrderItem = {
  name: string
  price: string
  quantity: number
}

type OrderPanelProps = {
  orderItems: OrderItem[]
  orderType: string
  total: number
  submitted: boolean
  onIncrease: (name: string) => void
  onDecrease: (name: string) => void
  onOrderTypeChange: (type: string) => void
  onSubmitOrder: () => void
}

function OrderPanel({
  orderItems,
  orderType,
  total,
  submitted,
  onIncrease,
  onDecrease,
  onOrderTypeChange,
  onSubmitOrder,
}: OrderPanelProps) {
  return (
    <aside className="order-panel">
      <h2>Your Order</h2>

      {orderItems.length === 0 ? (
        <p>No items added yet.</p>
      ) : (
        <>
          {orderItems.map((item) => (
            <div key={item.name} className="order-item">
              <h3>{item.name}</h3>
              <p>{item.price}</p>
              <div className="quantity-controls">
                <button onClick={() => onDecrease(item.name)}>-</button>
                <span>{item.quantity}</span>
                <button onClick={() => onIncrease(item.name)}>+</button>
              </div>
            </div>
          ))}

          <div className="order-type-section">
            <h3>Order Type</h3>
            <select
              value={orderType}
              onChange={(e) => onOrderTypeChange(e.target.value)}
            >
              <option value="Dine-In">Dine-In</option>
              <option value="Takeout">Takeout</option>
              <option value="Delivery">Delivery</option>
            </select>
          </div>

          <div className="order-summary">
            <h3>Total: ${total.toFixed(2)}</h3>
            <button onClick={onSubmitOrder}>Submit Order</button>
          </div>

          {submitted && (
            <p className="confirmation-message">
              Your {orderType.toLowerCase()} order has been submitted!
            </p>
          )}
        </>
      )}
    </aside>
  )
}

export default OrderPanel