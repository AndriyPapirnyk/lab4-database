from app.dao.gps_location_dao import GPSLocationDAO
from app.dtos.gps_location_dto import GPSLocationDTO
from datetime import datetime

class GPSLocationService:
    def __init__(self):
        self.dao = GPSLocationDAO()

    # READ ALL
    def get_all(self):
        locs = self.dao.get_all()
        return [l.to_dict() for l in locs]
        
    # READ BY ID
    def get_by_id(self, gps_id):
        loc = self.dao.get_by_id(gps_id)
        return loc.to_dict() if loc else None

    # CREATE
    def create(self, data):
        ts = data.get('timestamp', datetime.now())
        dto = GPSLocationDTO(None, data['field_id'], data['latitude'], data['longitude'], ts)
        return self.dao.create(dto)

    # UPDATE
    def update(self, gps_id, data):
        return self.dao.update(gps_id, data)

    # DELETE
    def delete(self, gps_id):
        return self.dao.delete(gps_id)