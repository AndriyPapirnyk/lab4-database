class SensorDTO:
    def __init__(self, sensor_id, field_id, type, model):
        self.sensor_id = sensor_id
        self.field_id = field_id
        self.type = type
        self.model = model
    def to_dict(self):
        return self.__dict__