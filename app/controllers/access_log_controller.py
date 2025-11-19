from flask import Blueprint, request, jsonify
from app.services.access_log_service import AccessLogService

log_bp = Blueprint('log', __name__)
service = AccessLogService()

# 1. READ ALL
@log_bp.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(service.get_all())

# 2. READ BY ID
@log_bp.route('/logs/<int:id>', methods=['GET'])
def get_log_by_id(id):
    data = service.get_by_id(id)
    if data: return jsonify(data)
    return jsonify({"message": "Log not found"}), 404

# 3. CREATE
@log_bp.route('/logs', methods=['POST'])
def create_log():
    if service.create(request.json):
        return jsonify({"message": "Log created"}), 201
    return jsonify({"message": "Error creating log"}), 400

# 4. UPDATE
@log_bp.route('/logs/<int:id>', methods=['PUT'])
def update_log(id):
    if service.update(id, request.json):
        return jsonify({"message": "Log updated"})
    return jsonify({"message": "Error updating log"}), 400

# 5. DELETE
@log_bp.route('/logs/<int:id>', methods=['DELETE'])
def delete_log(id):
    if service.delete(id):
        return jsonify({"message": "Log deleted"})
    return jsonify({"message": "Error deleting log"}), 400