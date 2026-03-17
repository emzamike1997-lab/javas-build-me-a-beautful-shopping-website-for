```python
from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User, UserSchema

user_blueprint = Blueprint('user', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@user_blueprint.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    result = user_schema.dump(user)
    return jsonify(result)

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    user = User(data['username'], data['email'], data['password'])
    db.session.add(user)
    db.session.commit()
    result = user_schema.dump(user)
    return jsonify(result), 201

@user_blueprint.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    user.username = data['username']
    user.email = data['email']
    db.session.commit()
    result = user_schema.dump(user)
    return jsonify(result)

@user_blueprint.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})
```

###