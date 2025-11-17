from flask import Blueprint, request, jsonify
from app.services.gps_location_service import GPSLocationService

gps_bp = Blueprint('gps', __name__)
service = GPSLocationService()

@gps_bp.route('/gps', methods=['GET'])
def get_gps():
    return jsonify(service.get_all())

@gps_bp.route('/gps', methods=['POST'])
def create_gps():
    if service.create(request.json):
        return jsonify({"message": "GPS location added"}), 201
    return jsonify({"message": "Error creating GPS location"}), 400