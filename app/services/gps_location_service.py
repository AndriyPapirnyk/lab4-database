from app.dao.gps_location_dao import GPSLocationDAO
from app.dtos.gps_location_dto import GPSLocationDTO
from datetime import datetime

class GPSLocationService:
    def __init__(self):
        self.dao = GPSLocationDAO()

    def get_all(self):
        locs = self.dao.get_all()
        return [l.to_dict() for l in locs]

    def create(self, data):
        ts = data.get('timestamp', datetime.now())
        dto = GPSLocationDTO(None, data['field_id'], data['latitude'], data['longitude'], ts)
        return self.dao.create(dto)