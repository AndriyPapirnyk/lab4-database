from flask import Blueprint, request, jsonify
from app.services.user_account_service import UserAccountService

user_bp = Blueprint('user', __name__)
service = UserAccountService()

# 1. READ ALL
@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(service.get_all())

# 2. READ BY ID
@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    data = service.get_by_id(id)
    if data: return jsonify(data)
    return jsonify({"message": "User not found"}), 404

# 3. CREATE
@user_bp.route('/users', methods=['POST'])
def create_user():
    if service.create(request.json):
        return jsonify({"message": "User created"}), 201
    return jsonify({"message": "Error creating user"}), 400

# 4. UPDATE
@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    if service.update(id, request.json):
        return jsonify({"message": "User updated"})
    return jsonify({"message": "Error updating user"}), 400

# 5. DELETE
@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if service.delete(id):
        return jsonify({"message": "User deleted"})
    return jsonify({"message": "Error deleting user"}), 400