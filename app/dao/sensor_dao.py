from app.db_config import get_db_connection
from app.dtos.sensor_dto import SensorDTO

class SensorDAO:
    # get_all, get_by_id, delete, update — реалізовані для таблиці Sensor (де немає field_id)
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Sensor")
        res = [SensorDTO(r['sensor_id'], r['type'], r['model']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res
    
    # ... (get_by_id, update, delete методи, адаптовані під відсутність field_id) ...
    
    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO Sensor (type, model) VALUES (%s, %s)" # field_id ВИДАЛЕНО
        try:
            cursor.execute(sql, (dto.type, dto.model))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()
    # ... (Інші CRUD методи) ...