```javascript
import React from 'react';
import { useParams } from 'react-router-dom';

function ProductDetails({ products }) {
  const { id } = useParams();
  const product = products.find(item => item.id === parseInt(id));

  if (!product) {
    return <p>Product not found.</p>;
  }

  return (
    <div>
      <h1>{product.name}</h1>
      <p>Price: {product.price}</p>
      <p>Description: {product.description}</p>
    </div>
  );
}

export default ProductDetails;
```

###