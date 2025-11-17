from app.db_config import get_db_connection
from app.dtos.user_account_dto import UserAccountDTO

class UserAccountDAO:
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM UserAccount")
        users = [UserAccountDTO(r['user_id'], r['client_id'], r['username'], r['password_hash'], r['role']) for r in cursor.fetchall()]
        cursor.close(); conn.close()
        return users

    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO UserAccount (client_id, username, password_hash, role) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (dto.client_id, dto.username, dto.password_hash, dto.role))
            conn.commit(); return True
        except Exception as e:
            print(f"DB Error: {e}")
            return False
        finally: cursor.close(); conn.close()