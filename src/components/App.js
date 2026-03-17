```javascript
import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './Header';
import Footer from './Footer';
import Home from './Home';
import Products from './Products';
import ProductDetails from './ProductDetails';
import Cart from './Cart';

function App() {
  const [cart, setCart] = useState([]);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('/api/products')
      .then(response => response.json())
      .then(data => setProducts(data));
  }, []);

  const handleAddToCart = product => {
    setCart([...cart, product]);
  };

  const handleRemoveFromCart = product => {
    setCart(cart.filter(item => item.id !== product.id));
  };

  return (
    <BrowserRouter>
      <Header cart={cart} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<Products products={products} />} />
        <Route
          path="/products/:id"
          element={<ProductDetails products={products} />}
        />
        <Route
          path="/cart"
          element={
            <Cart
              cart={cart}
              handleRemoveFromCart={handleRemoveFromCart}
            />
          }
        />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
```

###