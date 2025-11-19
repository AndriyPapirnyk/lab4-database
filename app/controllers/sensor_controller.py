from flask import Blueprint, request, jsonify
from app.services.sensor_service import SensorService

sensor_bp = Blueprint('sensor', __name__)
service = SensorService()

# 1. READ ALL
@sensor_bp.route('/sensors', methods=['GET'])
def get_sensors():
    return jsonify(service.get_all())

# 2. READ BY ID
@sensor_bp.route('/sensors/<int:id>', methods=['GET'])
def get_sensor_by_id(id):
    data = service.get_by_id(id)
    if data: return jsonify(data)
    return jsonify({"message": "Sensor not found"}), 404

# 3. CREATE
@sensor_bp.route('/sensors', methods=['POST'])
def create_sensor():
    if service.create(request.json):
        return jsonify({"message": "Sensor created"}), 201
    return jsonify({"message": "Error creating sensor"}), 400

# 4. UPDATE
@sensor_bp.route('/sensors/<int:id>', methods=['PUT'])
def update_sensor(id):
    if service.update(id, request.json):
        return jsonify({"message": "Sensor updated"})
    return jsonify({"message": "Error updating sensor"}), 400

# 5. DELETE
@sensor_bp.route('/sensors/<int:id>', methods=['DELETE'])
def delete_sensor(id):
    if service.delete(id):
        return jsonify({"message": "Sensor deleted"})
    return jsonify({"message": "Error deleting sensor"}), 400