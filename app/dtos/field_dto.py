class FieldDTO:
    def __init__(self, field_id, client_id, name, area, sensors=None):
        self.field_id = field_id
        self.client_id = client_id
        self.name = name
        self.area = float(area) if area else 0.0
        self.sensors = sensors if sensors else [] # Для вкладених даних

    def to_dict(self):
        return {
            "field_id": self.field_id,
            "client_id": self.client_id,
            "name": self.name,
            "area": self.area,
            "sensors": self.sensors
        }