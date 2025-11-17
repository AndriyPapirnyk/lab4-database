from app.db_config import get_db_connection
from app.dtos.gps_location_dto import GPSLocationDTO

class GPSLocationDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM GPSLocation")
        res = [GPSLocationDTO(r['gps_id'], r['field_id'], r['latitude'], r['longitude'], r['timestamp']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO GPSLocation (field_id, latitude, longitude, timestamp) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (dto.field_id, dto.latitude, dto.longitude, dto.timestamp))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()