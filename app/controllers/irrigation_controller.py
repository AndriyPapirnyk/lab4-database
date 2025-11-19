from flask import Blueprint, request, jsonify
from app.services.irrigation_service import IrrigationService

irrigation_bp = Blueprint('irrigation', __name__)
service = IrrigationService()

# 1. READ ALL
@irrigation_bp.route('/irrigations', methods=['GET'])
def get_irrigations():
    return jsonify(service.get_all())

# 2. READ BY ID
@irrigation_bp.route('/irrigations/<int:id>', methods=['GET'])
def get_irrigation_by_id(id):
    data = service.get_by_id(id)
    if data: return jsonify(data)
    return jsonify({"message": "Irrigation record not found"}), 404

# 3. CREATE
@irrigation_bp.route('/irrigations', methods=['POST'])
def create_irrigation():
    if service.create(request.json):
        return jsonify({"message": "Irrigation record created"}), 201
    return jsonify({"message": "Error creating irrigation record"}), 400

# 4. UPDATE
@irrigation_bp.route('/irrigations/<int:id>', methods=['PUT'])
def update_irrigation(id):
    if service.update(id, request.json):
        return jsonify({"message": "Irrigation record updated"})
    return jsonify({"message": "Error updating irrigation record"}), 400

# 5. DELETE
@irrigation_bp.route('/irrigations/<int:id>', methods=['DELETE'])
def delete_irrigation(id):
    if service.delete(id):
        return jsonify({"message": "Irrigation record deleted"})
    return jsonify({"message": "Error deleting irrigation record"}), 400