from app.dao.sprinkler_dao import SprinklerDAO
from app.dtos.sprinkler_dto import SprinklerDTO

class SprinklerService:
    def __init__(self):
        self.dao = SprinklerDAO()

    # READ ALL
    def get_all(self):
        sprinklers = self.dao.get_all()
        return [s.to_dict() for s in sprinklers]
        
    # READ BY ID
    def get_by_id(self, sprinkler_id):
        sprinkler = self.dao.get_by_id(sprinkler_id)
        return sprinkler.to_dict() if sprinkler else None

    # CREATE
    def create(self, data):
        dto = SprinklerDTO(None, data['field_id'], data['gps_id'], data['max_flow'])
        return self.dao.create(dto)

    # UPDATE
    def update(self, sprinkler_id, data):
        return self.dao.update(sprinkler_id, data)

    # DELETE
    def delete(self, sprinkler_id):
        return self.dao.delete(sprinkler_id)