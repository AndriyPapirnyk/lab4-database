from app.dao.field_dao import FieldDAO
from app.dtos.field_dto import FieldDTO

class FieldService:
    def __init__(self):
        self.dao = FieldDAO()

    def get_all_fields(self):
        fields = self.dao.get_all()
        return [f.to_dict() for f in fields]

    def create_field(self, data):
        # Валідація: площа не може бути від'ємною
        if float(data.get('area', 0)) < 0:
            return False
        new_field = FieldDTO(None, data['client_id'], data['name'], data['area'])
        return self.dao.create(new_field)

    def update_field(self, field_id, data):
        return self.dao.update(field_id, data)

    def delete_field(self, field_id):
        return self.dao.delete(field_id)
        
    def get_field_details(self, field_id):
        field = self.dao.get_field_with_sensors(field_id)
        return field.to_dict() if field else None