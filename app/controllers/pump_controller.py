from flask import Blueprint, request, jsonify
from app.services.pump_service import PumpService

pump_bp = Blueprint('pump', __name__)
service = PumpService()

@pump_bp.route('/pumps', methods=['GET'])
def get_pumps():
    return jsonify(service.get_all())

@pump_bp.route('/pumps', methods=['POST'])
def create_pump():
    if service.create(request.json):
        return jsonify({"message": "Pump created"}), 201
    return jsonify({"message": "Error creating pump"}), 400