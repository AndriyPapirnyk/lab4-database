from app.db_config import get_db_connection
from app.dtos.sprinkler_dto import SprinklerDTO

class SprinklerDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Sprinkler")
        res = [SprinklerDTO(r['sprinkler_id'], r['field_id'], r['gps_id'], r['max_flow']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return res

    def get_by_id(self, sprinkler_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Sprinkler WHERE sprinkler_id = %s", (sprinkler_id,))
        row = cursor.fetchone()
        sprinkler = SprinklerDTO(row['sprinkler_id'], row['field_id'], row['gps_id'], row['max_flow']) if row else None
        cursor.close(); conn.close()
        return sprinkler

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO Sprinkler (field_id, gps_id, max_flow) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.field_id, dto.gps_id, dto.max_flow))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()

    def update(self, sprinkler_id, data):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "UPDATE Sprinkler SET field_id=%s, gps_id=%s, max_flow=%s WHERE sprinkler_id=%s"
        try:
            cursor.execute(sql, (data.get('field_id'), data.get('gps_id'), data.get('max_flow'), sprinkler_id))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()

    def delete(self, sprinkler_id):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Sprinkler WHERE sprinkler_id=%s", (sprinkler_id,))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()