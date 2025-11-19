from app.db_config import get_db_connection
from app.dtos.sensor_data_dto import SensorDataDTO

class SensorDataDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM SensorData")
        res = [SensorDataDTO(r['data_id'], r['sensor_id'], r['value'], r['timestamp']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def get_by_id(self, data_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM SensorData WHERE data_id = %s", (data_id,))
        row = cursor.fetchone()
        data_rec = SensorDataDTO(row['data_id'], row['sensor_id'], row['value'], row['timestamp']) if row else None
        cursor.close(); conn.close()
        return data_rec

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO SensorData (sensor_id, value, timestamp) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.sensor_id, dto.value, dto.timestamp))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()

    def update(self, data_id, data):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "UPDATE SensorData SET sensor_id=%s, value=%s, timestamp=%s WHERE data_id=%s"
        try:
            cursor.execute(sql, (data.get('sensor_id'), data.get('value'), data.get('timestamp'), data_id))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()

    def delete(self, data_id):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM SensorData WHERE data_id=%s", (data_id,))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()