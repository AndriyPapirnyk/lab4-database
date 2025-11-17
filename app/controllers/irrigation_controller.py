from flask import Blueprint, request, jsonify
from app.services.irrigation_service import IrrigationService

irrigation_bp = Blueprint('irrigation', __name__)
service = IrrigationService()

@irrigation_bp.route('/irrigations', methods=['GET'])
def get_irrigations():
    return jsonify(service.get_all())

@irrigation_bp.route('/irrigations', methods=['POST'])
def create_irrigation():
    if service.create(request.json):
        return jsonify({"message": "Irrigation record created"}), 201
    return jsonify({"message": "Error creating irrigation record"}), 400