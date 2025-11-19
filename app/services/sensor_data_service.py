from app.dao.sensor_data_dao import SensorDataDAO
from app.dtos.sensor_data_dto import SensorDataDTO
from datetime import datetime

class SensorDataService:
    def __init__(self):
        self.dao = SensorDataDAO()

    # READ ALL
    def get_all(self):
        data_list = self.dao.get_all()
        return [d.to_dict() for d in data_list]
        
    # READ BY ID
    def get_by_id(self, data_id):
        data_rec = self.dao.get_by_id(data_id)
        return data_rec.to_dict() if data_rec else None

    # CREATE
    def create(self, data):
        ts = data.get('timestamp', datetime.now())
        dto = SensorDataDTO(None, data['sensor_id'], data['value'], ts)
        return self.dao.create(dto)

    # UPDATE
    def update(self, data_id, data):
        return self.dao.update(data_id, data)

    # DELETE
    def delete(self, data_id):
        return self.dao.delete(data_id)