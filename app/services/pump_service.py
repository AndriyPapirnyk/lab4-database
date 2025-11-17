from app.dao.pump_dao import PumpDAO
from app.dtos.pump_dto import PumpDTO

class PumpService:
    def __init__(self):
        self.dao = PumpDAO()

    def get_all(self):
        pumps = self.dao.get_all()
        return [p.to_dict() for p in pumps]

    def create(self, data):
        dto = PumpDTO(None, data['field_id'], data['model'], data['max_flow'])
        return self.dao.create(dto)