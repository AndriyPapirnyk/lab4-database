from app.dao.field_sensor_placement_dao import FieldSensorPlacementDAO
from app.dtos.field_sensor_placement_dto import FieldSensorPlacementDTO
from datetime import datetime

class FieldSensorPlacementService:
    def __init__(self): self.dao = FieldSensorPlacementDAO()
    def get_all(self): return [p.to_dict() for p in self.dao.get_all()]
    
    def get_by_ids(self, field_id, sensor_id):
        placement = self.dao.get_by_ids(field_id, sensor_id)
        return placement.to_dict() if placement else None

    def create(self, data):
        ts = data.get('placement_date', datetime.now())
        dto = FieldSensorPlacementDTO(data['field_id'], data['sensor_id'], ts)
        return self.dao.create(dto)

    def delete(self, field_id, sensor_id):
        return self.dao.delete(field_id, sensor_id)