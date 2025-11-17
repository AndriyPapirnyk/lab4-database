from app.db_config import get_db_connection
from app.dtos.access_log_dto import AccessLogDTO

class AccessLogDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM AccessLog")
        logs = [AccessLogDTO(r['log_id'], r['user_id'], r['action'], r['timestamp']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return logs

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO AccessLog (user_id, action, timestamp) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.user_id, dto.action, dto.timestamp))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()