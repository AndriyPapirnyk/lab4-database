from flask import Blueprint, request, jsonify
from app.services.pump_service import PumpService

pump_bp = Blueprint('pump', __name__)
service = PumpService()

# 1. READ ALL
@pump_bp.route('/pumps', methods=['GET'])
def get_pumps():
    return jsonify(service.get_all())

# 2. READ BY ID
@pump_bp.route('/pumps/<int:id>', methods=['GET'])
def get_pump_by_id(id):
    data = service.get_by_id(id)
    if data: return jsonify(data)
    return jsonify({"message": "Pump not found"}), 404

# 3. CREATE
@pump_bp.route('/pumps', methods=['POST'])
def create_pump():
    if service.create(request.json):
        return jsonify({"message": "Pump created"}), 201
    return jsonify({"message": "Error creating pump"}), 400

# 4. UPDATE
@pump_bp.route('/pumps/<int:id>', methods=['PUT'])
def update_pump(id):
    if service.update(id, request.json):
        return jsonify({"message": "Pump updated"})
    return jsonify({"message": "Error updating pump"}), 400

# 5. DELETE
@pump_bp.route('/pumps/<int:id>', methods=['DELETE'])
def delete_pump(id):
    if service.delete(id):
        return jsonify({"message": "Pump deleted"})
    return jsonify({"message": "Error deleting pump"}), 400

@pump_bp.route('/pumps/sp-insert', methods=['POST'])
def create_pump_via_sp():
    data = request.json
    if service.dao.call_insert_procedure(data['field_id'], data['model'], data['max_flow']):
        return jsonify({"message": "Pump created via Stored Procedure"}), 201
    return jsonify({"message": "Error creating pump (check trigger constraints?)"}), 400