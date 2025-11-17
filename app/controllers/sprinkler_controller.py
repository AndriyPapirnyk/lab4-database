from flask import Blueprint, request, jsonify
from app.services.sprinkler_service import SprinklerService

sprinkler_bp = Blueprint('sprinkler', __name__)
service = SprinklerService()

@sprinkler_bp.route('/sprinklers', methods=['GET'])
def get_sprinklers():
    return jsonify(service.get_all())

@sprinkler_bp.route('/sprinklers', methods=['POST'])
def create_sprinkler():
    if service.create(request.json):
        return jsonify({"message": "Sprinkler created"}), 201
    return jsonify({"message": "Error creating sprinkler"}), 400