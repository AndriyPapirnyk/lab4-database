from app.db_config import get_db_connection
from app.dtos.sensor_data_dto import SensorDataDTO

class SensorDataDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM SensorData")
        res = [SensorDataDTO(r['data_id'], r['sensor_id'], r['value'], r['timestamp']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO SensorData (sensor_id, value, timestamp) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.sensor_id, dto.value, dto.timestamp))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()