from flask import Flask

from app.controllers.client_controller import client_bp
from app.controllers.field_controller import field_bp
from app.controllers.user_account_controller import user_bp
from app.controllers.access_log_controller import log_bp
from app.controllers.gps_location_controller import gps_bp
from app.controllers.pump_controller import pump_bp
from app.controllers.irrigation_controller import irrigation_bp
from app.controllers.sensor_controller import sensor_bp
from app.controllers.sensor_data_controller import sensor_data_bp
from app.controllers.sprinkler_controller import sprinkler_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(client_bp)
    app.register_blueprint(field_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(log_bp)
    app.register_blueprint(gps_bp)
    app.register_blueprint(pump_bp)
    app.register_blueprint(irrigation_bp)
    app.register_blueprint(sensor_bp)
    app.register_blueprint(sensor_data_bp)
    app.register_blueprint(sprinkler_bp)
    
    return app