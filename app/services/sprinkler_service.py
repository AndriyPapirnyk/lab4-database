from app.dao.sprinkler_dao import SprinklerDAO
from app.dtos.sprinkler_dto import SprinklerDTO

class SprinklerService:
    def __init__(self):
        self.dao = SprinklerDAO()

    def get_all(self):
        sprinklers = self.dao.get_all()
        return [s.to_dict() for s in sprinklers]

    def create(self, data):
        dto = SprinklerDTO(None, data['field_id'], data['gps_id'], data['max_flow'])
        return self.dao.create(dto)