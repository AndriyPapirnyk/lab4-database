class GPSLocationDTO:
    def __init__(self, gps_id, field_id, latitude, longitude, timestamp):
        self.gps_id = gps_id
        self.field_id = field_id
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.timestamp = str(timestamp)
    def to_dict(self):
        return self.__dict__