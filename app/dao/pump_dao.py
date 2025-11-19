from app.db_config import get_db_connection
from app.dtos.pump_dto import PumpDTO

class PumpDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Pump")
        pumps = [PumpDTO(r['pump_id'], r['field_id'], r['model'], r['max_flow']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return pumps

    def get_by_id(self, pump_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Pump WHERE pump_id = %s", (pump_id,))
        row = cursor.fetchone()
        pump = PumpDTO(row['pump_id'], row['field_id'], row['model'], row['max_flow']) if row else None
        cursor.close(); conn.close()
        return pump

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO Pump (field_id, model, max_flow) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.field_id, dto.model, dto.max_flow))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()

    def update(self, pump_id, data):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "UPDATE Pump SET field_id=%s, model=%s, max_flow=%s WHERE pump_id=%s"
        try:
            cursor.execute(sql, (data.get('field_id'), data.get('model'), data.get('max_flow'), pump_id))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()

    def delete(self, pump_id):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Pump WHERE pump_id=%s", (pump_id,))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()