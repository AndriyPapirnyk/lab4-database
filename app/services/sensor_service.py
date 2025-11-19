from app.dao.sensor_dao import SensorDAO
from app.dtos.sensor_dto import SensorDTO

class SensorService:
    def __init__(self):
        self.dao = SensorDAO()

    # READ ALL
    def get_all(self):
        sensors = self.dao.get_all()
        return [s.to_dict() for s in sensors]
        
    # READ BY ID
    def get_by_id(self, sensor_id):
        sensor = self.dao.get_by_id(sensor_id)
        return sensor.to_dict() if sensor else None

    # CREATE
    def create(self, data):
        dto = SensorDTO(None, data['field_id'], data['type'], data['model'])
        return self.dao.create(dto)

    # UPDATE
    def update(self, sensor_id, data):
        return self.dao.update(sensor_id, data)

    # DELETE
    def delete(self, sensor_id):
        return self.dao.delete(sensor_id)