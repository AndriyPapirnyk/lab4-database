from app.db_config import get_db_connection
from app.dtos.user_account_dto import UserAccountDTO

class UserAccountDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM UserAccount")
        users = [UserAccountDTO(r['user_id'], r['client_id'], r['username'], r['password_hash'], r['role']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return users

    def get_by_id(self, user_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM UserAccount WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        user = UserAccountDTO(row['user_id'], row['client_id'], row['username'], row['password_hash'], row['role']) if row else None
        cursor.close(); conn.close()
        return user

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO UserAccount (client_id, username, password_hash, role) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (dto.client_id, dto.username, dto.password_hash, dto.role))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()

    def update(self, user_id, data):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "UPDATE UserAccount SET client_id=%s, username=%s, password_hash=%s, role=%s WHERE user_id=%s"
        try:
            cursor.execute(sql, (data.get('client_id'), data.get('username'), data.get('password_hash'), data.get('role'), user_id))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()

    def delete(self, user_id):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM UserAccount WHERE user_id=%s", (user_id,))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()