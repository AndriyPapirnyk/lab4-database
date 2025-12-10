from flask import Blueprint, request, jsonify
from app.services.field_sensor_placement_service import FieldSensorPlacementService

placement_bp = Blueprint('placement', __name__)
service = FieldSensorPlacementService()

# 1. READ ALL
@placement_bp.route('/placements', methods=['GET'])
def get_placements():
    return jsonify(service.get_all())

# 2. READ BY COMPOSITE ID (потрібні field_id та sensor_id у тілі запиту)
@placement_bp.route('/placements', methods=['GET'])
def get_placement_by_ids():
    field_id = request.args.get('field_id', type=int)
    sensor_id = request.args.get('sensor_id', type=int)
    if field_id is None or sensor_id is None:
        return jsonify({"message": "Missing field_id or sensor_id parameters"}), 400
        
    data = service.get_by_ids(field_id, sensor_id)
    if data: return jsonify(data)
    return jsonify({"message": "Placement not found"}), 404

# 3. CREATE
@placement_bp.route('/placements', methods=['POST'])
def create_placement():
    if service.create(request.json):
        return jsonify({"message": "Placement link created"}), 201
    return jsonify({"message": "Error creating placement"}), 400

# 4. DELETE (потрібні field_id та sensor_id у тілі запиту)
@placement_bp.route('/placements', methods=['DELETE'])
def delete_placement():
    data = request.json
    if not data or 'field_id' not in data or 'sensor_id' not in data:
        return jsonify({"message": "Missing field_id or sensor_id in body"}), 400
        
    if service.delete(data['field_id'], data['sensor_id']):
        return jsonify({"message": "Placement link deleted"})
    return jsonify({"message": "Error deleting placement"}), 400

# 2.b. Процедура: Зв'язок за назвами
@placement_bp.route('/placements/by-name', methods=['POST'])
def create_placement_by_name():
    data = request.json
    # Викликаємо DAO напряму для простоти (або додайте метод в Service)
    if service.dao.create_by_names(data['field_name'], data['sensor_model']):
        return jsonify({"message": "Placement created via SP (by Name)"}), 201
    return jsonify({"message": "Error (Check names or existing links)"}), 400