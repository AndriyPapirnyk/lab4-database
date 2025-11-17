from app.db_config import get_db_connection
from app.dtos.client_dto import ClientDTO

class ClientDAO:
    
    # Отримати всіх клієнтів
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) # dictionary=True повертає результат як словник
        cursor.execute("SELECT * FROM Client")
        rows = cursor.fetchall()
        
        clients = [ClientDTO(row['client_id'], row['name'], row['phone'], row['email']) for row in rows]
        
        cursor.close()
        conn.close()
        return clients

    # Створити клієнта
    def create(self, client_dto):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO Client (name, phone, email) VALUES (%s, %s, %s)"
        val = (client_dto.name, client_dto.phone, client_dto.email)
        
        try:
            cursor.execute(sql, val)
            conn.commit()
            created = True
        except Exception as e:
            print(f"Error: {e}")
            created = False
        finally:
            cursor.close()
            conn.close()
        return created

    # Оновити клієнта
    def update(self, client_id, data):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "UPDATE Client SET name=%s, phone=%s, email=%s WHERE client_id=%s"
        val = (data['name'], data['phone'], data['email'], client_id)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()
        return True

    # Видалити клієнта
    def delete(self, client_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        # Увага: через FOREIGN KEY спочатку треба видаляти залежні записи або мати ON DELETE CASCADE
        # Для простоти припустимо, що ми видаляємо тільки клієнта
        try:
            cursor.execute("DELETE FROM Client WHERE client_id = %s", (client_id,))
            conn.commit()
            success = True
        except Exception as e:
            print(f"Cannot delete: {e}")
            success = False
            
        cursor.close()
        conn.close()
        return success

    # СКЛАДНИЙ ЗАПИТ (M:1): Отримати клієнта разом з його полями
    def get_client_with_fields(self, client_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Спочатку беремо клієнта
        cursor.execute("SELECT * FROM Client WHERE client_id = %s", (client_id,))
        client_row = cursor.fetchone()
        
        if not client_row:
            return None
            
        # Тепер беремо його поля (Fields)
        cursor.execute("SELECT field_id, name, area FROM Field WHERE client_id = %s", (client_id,))
        field_rows = cursor.fetchall()
        
        # Формуємо список словників для полів
        fields_list = [{"field_id": f['field_id'], "name": f['name'], "area": float(f['area'])} for f in field_rows]
        
        client_dto = ClientDTO(client_row['client_id'], client_row['name'], client_row['phone'], client_row['email'], fields_list)
        
        cursor.close()
        conn.close()
        return client_dto