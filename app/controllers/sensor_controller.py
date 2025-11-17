from flask import Blueprint, request, jsonify
from app.services.sensor_service import SensorService

sensor_bp = Blueprint('sensor', __name__)
service = SensorService()

@sensor_bp.route('/sensors', methods=['GET'])
def get_sensors():
    return jsonify(service.get_all())

@sensor_bp.route('/sensors', methods=['POST'])
def create_sensor():
    if service.create(request.json):
        return jsonify({"message": "Sensor created"}), 201
    return jsonify({"message": "Error creating sensor"}), 400