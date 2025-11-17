from app.dao.sensor_data_dao import SensorDataDAO
from app.dtos.sensor_data_dto import SensorDataDTO
from datetime import datetime

class SensorDataService:
    def __init__(self):
        self.dao = SensorDataDAO()

    def get_all(self):
        data_list = self.dao.get_all()
        return [d.to_dict() for d in data_list]

    def create(self, data):
        ts = data.get('timestamp', datetime.now())
        dto = SensorDataDTO(None, data['sensor_id'], data['value'], ts)
        return self.dao.create(dto)