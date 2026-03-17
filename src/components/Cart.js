```javascript
import React from 'react';

function Cart({ cart, handleRemoveFromCart }) {
  return (
    <div>
      <h1>Cart</h1>
      <ul>
        {cart.map(product => (
          <li key={product.id}>
            {product.name} ({product.price})
            <button onClick={() => handleRemoveFromCart(product)}>
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Cart;
```

###