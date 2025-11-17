from flask import Blueprint, request, jsonify
from app.services.user_account_service import UserAccountService

user_bp = Blueprint('user', __name__)
service = UserAccountService()

@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(service.get_all())

@user_bp.route('/users', methods=['POST'])
def create_user():
    if service.create(request.json):
        return jsonify({"message": "User created"}), 201
    return jsonify({"message": "Error creating user"}), 400