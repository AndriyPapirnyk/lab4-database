from app.db_config import get_db_connection
from app.dtos.pump_dto import PumpDTO

class PumpDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Pump")
        pumps = [PumpDTO(r['pump_id'], r['field_id'], r['model'], r['max_flow']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return pumps

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO Pump (field_id, model, max_flow) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.field_id, dto.model, dto.max_flow))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()