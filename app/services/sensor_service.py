from app.dao.sensor_dao import SensorDAO
from app.dtos.sensor_dto import SensorDTO

class SensorService:
    def __init__(self):
        self.dao = SensorDAO()

    def get_all(self):
        sensors = self.dao.get_all()
        return [s.to_dict() for s in sensors]

    def create(self, data):
        dto = SensorDTO(None, data['field_id'], data['type'], data['model'])
        return self.dao.create(dto)