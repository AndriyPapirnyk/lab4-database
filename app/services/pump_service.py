from app.dao.pump_dao import PumpDAO
from app.dtos.pump_dto import PumpDTO

class PumpService:
    def __init__(self):
        self.dao = PumpDAO()

    # READ ALL
    def get_all(self):
        pumps = self.dao.get_all()
        return [p.to_dict() for p in pumps]

    # READ BY ID
    def get_by_id(self, pump_id):
        pump = self.dao.get_by_id(pump_id)
        return pump.to_dict() if pump else None

    # CREATE
    def create(self, data):
        dto = PumpDTO(None, data['field_id'], data['model'], data['max_flow'])
        return self.dao.create(dto)

    # UPDATE
    def update(self, pump_id, data):
        return self.dao.update(pump_id, data)

    # DELETE
    def delete(self, pump_id):
        return self.dao.delete(pump_id)