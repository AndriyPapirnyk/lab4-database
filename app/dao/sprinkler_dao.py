from app.db_config import get_db_connection
from app.dtos.sprinkler_dto import SprinklerDTO

class SprinklerDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Sprinkler")
        res = [SprinklerDTO(r['sprinkler_id'], r['field_id'], r['gps_id'], r['max_flow']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO Sprinkler (field_id, gps_id, max_flow) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.field_id, dto.gps_id, dto.max_flow))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()