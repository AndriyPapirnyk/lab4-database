from app.dao.irrigation_dao import IrrigationDAO
from app.dtos.irrigation_dto import IrrigationDTO

class IrrigationService:
    def __init__(self):
        self.dao = IrrigationDAO()

    def get_all(self):
        items = self.dao.get_all()
        return [i.to_dict() for i in items]

    def create(self, data):
        # duration_minutes та total_volume розраховуються базою даних автоматично
        dto = IrrigationDTO(None, data['pump_id'], data['start_time'], data['end_time'], data['flow_rate'])
        return self.dao.create(dto)