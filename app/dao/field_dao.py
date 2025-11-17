from app.db_config import get_db_connection
from app.dtos.field_dto import FieldDTO

class FieldDAO:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Field")
        rows = cursor.fetchall()
        fields = [FieldDTO(row['field_id'], row['client_id'], row['name'], row['area']) for row in rows]
        cursor.close()
        conn.close()
        return fields

    def create(self, field_dto):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO Field (client_id, name, area) VALUES (%s, %s, %s)"
        val = (field_dto.client_id, field_dto.name, field_dto.area)
        try:
            cursor.execute(sql, val)
            conn.commit()
            result = True
        except Exception as e:
            print(f"Error creating field: {e}")
            result = False
        finally:
            cursor.close()
            conn.close()
        return result

    def update(self, field_id, data):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "UPDATE Field SET name=%s, area=%s WHERE field_id=%s"
        val = (data['name'], data['area'], field_id)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def delete(self, field_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Field WHERE field_id = %s", (field_id,))
            conn.commit()
            result = True
        except Exception as e:
            print(f"Error deleting field: {e}")
            result = False
        cursor.close()
        conn.close()
        return result

    # Складний запит: Отримати поле разом з усіма його сенсорами (M:1 для Field->Sensor)
    def get_field_with_sensors(self, field_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # 1. Отримати поле
        cursor.execute("SELECT * FROM Field WHERE field_id = %s", (field_id,))
        field_row = cursor.fetchone()
        if not field_row:
            return None
            
        # 2. Отримати всі сенсори цього поля
        cursor.execute("SELECT sensor_id, type, model FROM Sensor WHERE field_id = %s", (field_id,))
        sensor_rows = cursor.fetchall()
        
        sensors_list = [{"id": s['sensor_id'], "type": s['type'], "model": s['model']} for s in sensor_rows]
        
        field_dto = FieldDTO(field_row['field_id'], field_row['client_id'], field_row['name'], field_row['area'], sensors_list)
        
        cursor.close()
        conn.close()
        return field_dto