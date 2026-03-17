```javascript
import React from 'react';
import { Link } from 'react-router-dom';

function Header({ cart }) {
  return (
    <header>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/products">Products</Link>
          </li>
          <li>
            <Link to="/cart">Cart ({cart.length})</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
```

###