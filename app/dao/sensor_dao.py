from app.db_config import get_db_connection
from app.dtos.sensor_dto import SensorDTO

class SensorDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Sensor")
        res = [SensorDTO(r['sensor_id'], r['field_id'], r['type'], r['model']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def get_by_id(self, sensor_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Sensor WHERE sensor_id = %s", (sensor_id,))
        row = cursor.fetchone()
        sensor = SensorDTO(row['sensor_id'], row['field_id'], row['type'], row['model']) if row else None
        cursor.close(); conn.close()
        return sensor

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO Sensor (field_id, type, model) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.field_id, dto.type, dto.model))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()

    def update(self, sensor_id, data):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "UPDATE Sensor SET field_id=%s, type=%s, model=%s WHERE sensor_id=%s"
        try:
            cursor.execute(sql, (data.get('field_id'), data.get('type'), data.get('model'), sensor_id))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()

    def delete(self, sensor_id):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Sensor WHERE sensor_id=%s", (sensor_id,))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()