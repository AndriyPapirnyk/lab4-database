class SensorDataDTO:
    def __init__(self, data_id, sensor_id, value, timestamp):
        self.data_id = data_id
        self.sensor_id = sensor_id
        self.value = float(value)
        self.timestamp = str(timestamp)
    def to_dict(self):
        return self.__dict__