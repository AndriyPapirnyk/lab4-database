from app.db_config import get_db_connection
from app.dtos.access_log_dto import AccessLogDTO

class AccessLogDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM AccessLog")
        logs = [AccessLogDTO(r['log_id'], r['user_id'], r['action'], r['timestamp']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return logs

    def get_by_id(self, log_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM AccessLog WHERE log_id = %s", (log_id,))
        row = cursor.fetchone()
        log = AccessLogDTO(row['log_id'], row['user_id'], row['action'], row['timestamp']) if row else None
        cursor.close(); conn.close()
        return log

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO AccessLog (user_id, action, timestamp) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.user_id, dto.action, dto.timestamp))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()

    def update(self, log_id, data):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "UPDATE AccessLog SET user_id=%s, action=%s, timestamp=%s WHERE log_id=%s"
        try:
            cursor.execute(sql, (data.get('user_id'), data.get('action'), data.get('timestamp'), log_id))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()

    def delete(self, log_id):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM AccessLog WHERE log_id=%s", (log_id,))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()