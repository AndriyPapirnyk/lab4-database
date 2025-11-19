from flask import Blueprint, request, jsonify
from app.services.sensor_data_service import SensorDataService

sensor_data_bp = Blueprint('sensor_data', __name__)
service = SensorDataService()

# 1. READ ALL
@sensor_data_bp.route('/sensor-data', methods=['GET'])
def get_data():
    return jsonify(service.get_all())

# 2. READ BY ID
@sensor_data_bp.route('/sensor-data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    data = service.get_by_id(id)
    if data: return jsonify(data)
    return jsonify({"message": "Sensor data record not found"}), 404

# 3. CREATE
@sensor_data_bp.route('/sensor-data', methods=['POST'])
def create_data():
    if service.create(request.json):
        return jsonify({"message": "Sensor data recorded"}), 201
    return jsonify({"message": "Error recording data"}), 400

# 4. UPDATE
@sensor_data_bp.route('/sensor-data/<int:id>', methods=['PUT'])
def update_data(id):
    if service.update(id, request.json):
        return jsonify({"message": "Sensor data updated"})
    return jsonify({"message": "Error updating sensor data"}), 400

# 5. DELETE
@sensor_data_bp.route('/sensor-data/<int:id>', methods=['DELETE'])
def delete_data(id):
    if service.delete(id):
        return jsonify({"message": "Sensor data deleted"})
    return jsonify({"message": "Error deleting sensor data"}), 400