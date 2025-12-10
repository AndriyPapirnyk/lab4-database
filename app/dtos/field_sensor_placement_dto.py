class FieldSensorPlacementDTO:
    # Додано параметр sensor_details
    def __init__(self, field_id, sensor_id, placement_date, sensor_details=None):
        self.field_id = field_id
        self.sensor_id = sensor_id
        self.placement_date = str(placement_date)
        self.sensor_details = sensor_details if sensor_details else {}

    def to_dict(self):
        # Якщо ми маємо деталі сенсора, форматуємо вивід, замінюючи сирий sensor_id на об'єкт.
        if self.sensor_details:
            return {
                "field_id": self.field_id,
                "placement_date": self.placement_date,
                "sensor": self.sensor_details # Вкладений об'єкт з даними сенсора
            }
        return self.__dict__