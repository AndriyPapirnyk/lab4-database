from app.db_config import get_db_connection
from app.dtos.client_dto import ClientDTO

class ClientDAO:
    
    # Отримати всіх клієнтів
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) 
        cursor.execute("SELECT * FROM Client")
        rows = cursor.fetchall()
        
        clients = [ClientDTO(row['client_id'], row['name'], row['phone'], row['email']) for row in rows]
        
        cursor.close()
        conn.close()
        return clients

    # Читання за ID
    def get_by_id(self, client_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Виконуємо SELECT WHERE ID
        cursor.execute("SELECT * FROM Client WHERE client_id = %s", (client_id,))
        row = cursor.fetchone()
        
        # Перетворюємо результат у DTO
        client = ClientDTO(row['client_id'], row['name'], row['phone'], row['email']) if row else None
        
        cursor.close()
        conn.close()
        return client

    # Створити клієнта
    def create(self, client_dto):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO Client (name, phone, email) VALUES (%s, %s, %s)"
        val = (client_dto.name, client_dto.phone, client_dto.email)
        
        try:
            cursor.execute(sql, val)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error (CREATE): {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    # Оновити клієнта
    def update(self, client_id, data):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "UPDATE Client SET name=%s, phone=%s, email=%s WHERE client_id=%s"
        val = (data['name'], data['phone'], data['email'], client_id)
        
        try:
            cursor.execute(sql, val)
            conn.commit()
            # Перевіряємо, чи був оновлений хоча б один рядок
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error (UPDATE): {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    # Видалити клієнта
    def delete(self, client_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Client WHERE client_id = %s", (client_id,))
            conn.commit()
            # Перевіряємо, чи був видалений хоча б один рядок
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error (DELETE): {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    # СКЛАДНИЙ ЗАПИТ (M:1): Отримати клієнта разом з його полями
    def get_client_with_fields(self, client_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM Client WHERE client_id = %s", (client_id,))
        client_row = cursor.fetchone()
        if not client_row:
            return None
            
        cursor.execute("SELECT field_id, name, area FROM Field WHERE client_id = %s", (client_id,))
        field_rows = cursor.fetchall()
        
        fields_list = [{"field_id": f['field_id'], "name": f['name'], "area": float(f['area'])} for f in field_rows]
        
        client_dto = ClientDTO(client_row['client_id'], client_row['name'], client_row['phone'], client_row['email'], fields_list)
        
        cursor.close()
        conn.close()
        return client_dto
    
    def call_bulk_insert(self):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.callproc('BulkInsertClients')
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()