from flask import Blueprint, request, jsonify
from app.services.client_service import ClientService

client_bp = Blueprint('client', __name__)
service = ClientService()

# 1. Отримати всіх (GET)
@client_bp.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(service.get_all_clients())

# Маршрут для отримання одного клієнта за ID
@client_bp.route('/clients/<int:id>', methods=['GET'])
def get_client_by_id(id):
    data = service.get_by_id(id)
    if data: return jsonify(data)
    return jsonify({"message": "Client not found"}), 404

# 2. Створити нового (POST)
@client_bp.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    if service.create_client(data):
        return jsonify({"message": "Client created successfully"}), 201
    return jsonify({"message": "Error creating client"}), 400

# 3. Оновити (PUT)
@client_bp.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    data = request.json
    service.update_client(id, data)
    return jsonify({"message": "Client updated"})

# 4. Видалити (DELETE)
@client_bp.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    if service.delete_client(id):
        return jsonify({"message": "Client deleted"})
    return jsonify({"message": "Cannot delete client (probably has linked data)"}), 400

# 5. Складний запит (Клієнт + його Поля)
@client_bp.route('/clients/<int:id>/fields', methods=['GET'])
def get_client_with_fields(id):
    data = service.get_client_details(id)
    if data:
        return jsonify(data)
    return jsonify({"message": "Client not found"}), 404

@client_bp.route('/clients/bulk-sp', methods=['POST'])
def bulk_insert_clients():
    if service.dao.call_bulk_insert():
        return jsonify({"message": "10 Clients inserted via SP"}), 201
    return jsonify({"message": "Error"}), 400