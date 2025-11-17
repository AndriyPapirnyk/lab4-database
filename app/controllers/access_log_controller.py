from flask import Blueprint, request, jsonify
from app.services.access_log_service import AccessLogService

log_bp = Blueprint('log', __name__)
service = AccessLogService()

@log_bp.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(service.get_all())

@log_bp.route('/logs', methods=['POST'])
def create_log():
    if service.create(request.json):
        return jsonify({"message": "Log entry created"}), 201
    return jsonify({"message": "Error creating log"}), 400