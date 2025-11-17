from flask import Blueprint, request, jsonify
from app.services.sensor_data_service import SensorDataService

sensor_data_bp = Blueprint('sensor_data', __name__)
service = SensorDataService()

@sensor_data_bp.route('/sensor-data', methods=['GET'])
def get_data():
    return jsonify(service.get_all())

@sensor_data_bp.route('/sensor-data', methods=['POST'])
def create_data():
    if service.create(request.json):
        return jsonify({"message": "Sensor data recorded"}), 201
    return jsonify({"message": "Error recording data"}), 400