from app.db_config import get_db_connection
from app.dtos.irrigation_dto import IrrigationDTO

class IrrigationDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Irrigation")
        res = [IrrigationDTO(r['irrigation_id'], r['pump_id'], r['start_time'], r['end_time'], r['flow_rate'], r['duration_minutes'], r['total_volume']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def get_by_id(self, irrigation_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Irrigation WHERE irrigation_id = %s", (irrigation_id,))
        row = cursor.fetchone()
        item = IrrigationDTO(row['irrigation_id'], row['pump_id'], row['start_time'], row['end_time'], row['flow_rate'], row['duration_minutes'], row['total_volume']) if row else None
        cursor.close(); conn.close()
        return item

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO Irrigation (pump_id, start_time, end_time, flow_rate) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (dto.pump_id, dto.start_time, dto.end_time, dto.flow_rate))
            conn.commit(); return True
        except Exception as e:
            print(f"DB Error (CREATE): {e}"); return False
        finally: cursor.close(); conn.close()

    def update(self, irrigation_id, data):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "UPDATE Irrigation SET pump_id=%s, start_time=%s, end_time=%s, flow_rate=%s WHERE irrigation_id=%s"
        try:
            cursor.execute(sql, (data.get('pump_id'), data.get('start_time'), data.get('end_time'), data.get('flow_rate'), irrigation_id))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()

    def delete(self, irrigation_id):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Irrigation WHERE irrigation_id=%s", (irrigation_id,))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()