from app.db_config import get_db_connection
from app.dtos.sensor_dto import SensorDTO

class SensorDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Sensor")
        res = [SensorDTO(r['sensor_id'], r['field_id'], r['type'], r['model']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO Sensor (field_id, type, model) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.field_id, dto.type, dto.model))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()