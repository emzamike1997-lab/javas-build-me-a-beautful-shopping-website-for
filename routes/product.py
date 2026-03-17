```python
from flask import Blueprint, request, jsonify
from app import db
from app.models.product import Product, ProductSchema

product_blueprint = Blueprint('product', __name__)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_blueprint.route('/products', methods=['GET'])
def get_all_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

@product_blueprint.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product is None:
        return jsonify({'message': 'Product not found'}), 404
    result = product_schema.dump(product)
    return jsonify(result)

@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    product = Product(data['name'], data['description'], data['price'], data['image_url'])
    db.session.add(product)
    db.session.commit()
    result = product_schema.dump(product)
    return jsonify(result), 201

@product_blueprint.route('/products/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if product is None:
        return jsonify({'message': 'Product not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.image_url = data['image_url']
    db.session.commit()
    result = product_schema.dump(product)
    return jsonify(result)

@product_blueprint.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product is None:
        return jsonify({'message': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})
```

###