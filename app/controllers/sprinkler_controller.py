from flask import Blueprint, request, jsonify
from app.services.sprinkler_service import SprinklerService

sprinkler_bp = Blueprint('sprinkler', __name__)
service = SprinklerService()

# 1. READ ALL
@sprinkler_bp.route('/sprinklers', methods=['GET'])
def get_sprinklers():
    return jsonify(service.get_all())

# 2. READ BY ID
@sprinkler_bp.route('/sprinklers/<int:id>', methods=['GET'])
def get_sprinkler_by_id(id):
    data = service.get_by_id(id)
    if data: return jsonify(data)
    return jsonify({"message": "Sprinkler not found"}), 404

# 3. CREATE
@sprinkler_bp.route('/sprinklers', methods=['POST'])
def create_sprinkler():
    if service.create(request.json):
        return jsonify({"message": "Sprinkler created"}), 201
    return jsonify({"message": "Error creating sprinkler"}), 400

# 4. UPDATE
@sprinkler_bp.route('/sprinklers/<int:id>', methods=['PUT'])
def update_sprinkler(id):
    if service.update(id, request.json):
        return jsonify({"message": "Sprinkler updated"})
    return jsonify({"message": "Error updating sprinkler"}), 400

# 5. DELETE
@sprinkler_bp.route('/sprinklers/<int:id>', methods=['DELETE'])
def delete_sprinkler(id):
    if service.delete(id):
        return jsonify({"message": "Sprinkler deleted"})
    return jsonify({"message": "Error deleting sprinkler"}), 400