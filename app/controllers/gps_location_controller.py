from flask import Blueprint, request, jsonify
from app.services.gps_location_service import GPSLocationService

gps_bp = Blueprint('gps', __name__)
service = GPSLocationService()

# 1. READ ALL
@gps_bp.route('/gps', methods=['GET'])
def get_gps():
    return jsonify(service.get_all())

# 2. READ BY ID
@gps_bp.route('/gps/<int:id>', methods=['GET'])
def get_gps_by_id(id):
    data = service.get_by_id(id)
    if data: return jsonify(data)
    return jsonify({"message": "GPS location not found"}), 404

# 3. CREATE
@gps_bp.route('/gps', methods=['POST'])
def create_gps():
    if service.create(request.json):
        return jsonify({"message": "GPS location created"}), 201
    return jsonify({"message": "Error creating GPS location"}), 400

# 4. UPDATE
@gps_bp.route('/gps/<int:id>', methods=['PUT'])
def update_gps(id):
    if service.update(id, request.json):
        return jsonify({"message": "GPS location updated"})
    return jsonify({"message": "Error updating GPS location"}), 400

# 5. DELETE
@gps_bp.route('/gps/<int:id>', methods=['DELETE'])
def delete_gps(id):
    if service.delete(id):
        return jsonify({"message": "GPS location deleted"})
    return jsonify({"message": "Error deleting GPS location"}), 400