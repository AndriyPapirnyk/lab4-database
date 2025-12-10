from flask import Blueprint, request, jsonify
from app.services.field_service import FieldService

field_bp = Blueprint('field', __name__)
service = FieldService()

@field_bp.route('/fields', methods=['GET'])
def get_fields():
    return jsonify(service.get_all_fields())

@field_bp.route('/fields', methods=['POST'])
def create_field():
    data = request.json
    if service.create_field(data):
        return jsonify({"message": "Field created"}), 201
    return jsonify({"message": "Error creating field"}), 400

@field_bp.route('/fields/<int:id>', methods=['PUT'])
def update_field(id):
    data = request.json
    service.update_field(id, data)
    return jsonify({"message": "Field updated"})

@field_bp.route('/fields/<int:id>', methods=['DELETE'])
def delete_field(id):
    if service.delete_field(id):
        return jsonify({"message": "Field deleted"})
    return jsonify({"message": "Error deleting field"}), 400

# Реалізація складного виводу (Поле + Сенсори)
@field_bp.route('/fields/<int:id>/sensors', methods=['GET'])
def get_field_sensors(id):
    data = service.get_field_details(id)
    if data:
        return jsonify(data)
    return jsonify({"message": "Field not found"}), 404

# 2.d. Маршрут для статистики
@field_bp.route('/fields/stats', methods=['GET'])
def get_field_stats():
    op = request.args.get('op', 'AVG') # За замовчуванням AVG
    result = service.dao.get_stats(op)
    if result: return jsonify(result)
    return jsonify({"message": "Error calculating stats"}), 400

# 2.e. Маршрут для запуску курсора
@field_bp.route('/fields/cursor-split', methods=['POST'])
def run_cursor():
    if service.dao.run_cursor_split():
        return jsonify({"message": "Cursor executed. Dynamic tables created."}), 201
    return jsonify({"message": "Error running cursor"}), 400