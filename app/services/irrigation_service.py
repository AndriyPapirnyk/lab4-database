from app.dao.irrigation_dao import IrrigationDAO
from app.dtos.irrigation_dto import IrrigationDTO

class IrrigationService:
    def __init__(self):
        self.dao = IrrigationDAO()

    # READ ALL
    def get_all(self):
        items = self.dao.get_all()
        return [i.to_dict() for i in items]
        
    # READ BY ID
    def get_by_id(self, irrigation_id):
        item = self.dao.get_by_id(irrigation_id)
        return item.to_dict() if item else None

    # CREATE
    def create(self, data):
        # duration_minutes та total_volume розраховуються базою даних
        dto = IrrigationDTO(None, data['pump_id'], data['start_time'], data['end_time'], data['flow_rate'])
        return self.dao.create(dto)

    # UPDATE
    def update(self, irrigation_id, data):
        return self.dao.update(irrigation_id, data)

    # DELETE
    def delete(self, irrigation_id):
        return self.dao.delete(irrigation_id)