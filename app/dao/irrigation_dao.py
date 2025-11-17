from app.db_config import get_db_connection
from app.dtos.irrigation_dto import IrrigationDTO

class IrrigationDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Irrigation")
        # Тут читаємо всі поля, включаючи згенеровані
        res = [IrrigationDTO(r['irrigation_id'], r['pump_id'], r['start_time'], r['end_time'], r['flow_rate'], r['duration_minutes'], r['total_volume']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        # ТІЛЬКИ вхідні параметри
        sql = "INSERT INTO Irrigation (pump_id, start_time, end_time, flow_rate) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (dto.pump_id, dto.start_time, dto.end_time, dto.flow_rate))
            conn.commit(); return True
        except Exception as e:
            print(f"DB Error: {e}")
            return False
        finally: cursor.close(); conn.close()