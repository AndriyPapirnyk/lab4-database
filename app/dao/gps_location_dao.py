from app.db_config import get_db_connection
from app.dtos.gps_location_dto import GPSLocationDTO

class GPSLocationDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM GPSLocation")
        res = [GPSLocationDTO(r['gps_id'], r['field_id'], r['latitude'], r['longitude'], r['timestamp']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def get_by_id(self, gps_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM GPSLocation WHERE gps_id = %s", (gps_id,))
        row = cursor.fetchone()
        gps = GPSLocationDTO(row['gps_id'], row['field_id'], row['latitude'], row['longitude'], row['timestamp']) if row else None
        cursor.close(); conn.close()
        return gps

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO GPSLocation (field_id, latitude, longitude, timestamp) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (dto.field_id, dto.latitude, dto.longitude, dto.timestamp))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()

    def update(self, gps_id, data):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "UPDATE GPSLocation SET field_id=%s, latitude=%s, longitude=%s, timestamp=%s WHERE gps_id=%s"
        try:
            cursor.execute(sql, (data.get('field_id'), data.get('latitude'), data.get('longitude'), data.get('timestamp'), gps_id))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()

    def delete(self, gps_id):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM GPSLocation WHERE gps_id=%s", (gps_id,))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()