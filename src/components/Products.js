```javascript
import React from 'react';
import { Link } from 'react-router-dom';

function Products({ products }) {
  return (
    <div>
      <h1>Products</h1>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <Link to={`/products/${product.id}`}>
              {product.name} (${product.price})
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Products;
```

###