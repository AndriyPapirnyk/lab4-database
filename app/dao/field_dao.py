from app.db_config import get_db_connection
from app.dtos.field_dto import FieldDTO

class FieldDAO:
    # 1. READ ALL
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Field")
        rows = cursor.fetchall()
        fields = [FieldDTO(r['field_id'], r['client_id'], r['name'], r['area']) for r in rows]
        cursor.close(); conn.close()
        return fields

    # 2. READ BY ID
    def get_by_id(self, field_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Field WHERE field_id = %s", (field_id,))
        row = cursor.fetchone()
        field = FieldDTO(row['field_id'], row['client_id'], row['name'], row['area']) if row else None
        cursor.close(); conn.close()
        return field

    # 3. CREATE
    def create(self, dto):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "INSERT INTO Field (client_id, name, area) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (dto.client_id, dto.name, dto.area))
            conn.commit(); return True
        except: return False
        finally: cursor.close(); conn.close()

    # 4. UPDATE
    def update(self, field_id, data):
        conn = get_db_connection(); cursor = conn.cursor()
        sql = "UPDATE Field SET client_id=%s, name=%s, area=%s WHERE field_id=%s"
        try:
            cursor.execute(sql, (data.get('client_id'), data.get('name'), data.get('area'), field_id))
            conn.commit(); return cursor.rowcount > 0
        except: return False
        finally: cursor.close(); conn.close()

    # 5. DELETE (Цей метод був відсутній!)
    def delete(self, field_id):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Field WHERE field_id=%s", (field_id,))
            conn.commit(); return cursor.rowcount > 0
        except Exception as e: 
            print(f"Error deleting field: {e}")
            return False
        finally: cursor.close(); conn.close()

    # --- СКЛАДНІ ЗАПИТИ ---

    # M:M Складний запит: отримати всі сенсори для поля через стикувальну таблицю
    def get_field_with_sensors(self, field_id):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Field WHERE field_id = %s", (field_id,))
        field_row = cursor.fetchone()
        if not field_row: return None
        
        # JOIN через Field_Sensor_Placement
        sql_sensors = """
            SELECT 
                S.sensor_id, S.type, S.model, P.placement_date
            FROM Sensor S
            JOIN Field_Sensor_Placement P ON S.sensor_id = P.sensor_id
            WHERE P.field_id = %s
        """
        cursor.execute(sql_sensors, (field_id,))
        
        sensors_list = [
            {"id": s['sensor_id'], "type": s['type'], "model": s['model'], "placement_date": str(s['placement_date'])} 
            for s in cursor.fetchall()
        ]
        
        field_dto = FieldDTO(field_row['field_id'], field_row['client_id'], field_row['name'], field_row['area'], sensors_list)
        cursor.close(); conn.close()
        return field_dto

    # --- STORED PROCEDURES ---

    # Виклик функції статистики
    def get_stats(self, operation):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        try:
            cursor.callproc('GetFieldStats', [operation])
            for result in cursor.stored_results():
                return result.fetchone()
        except Exception as e:
            print(f"Stats Error: {e}")
            return None
        finally: cursor.close(); conn.close()

    # Виклик Курсора
    def run_cursor_split(self):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.callproc('SplitFieldDataCursor')
            conn.commit()
            return True
        except Exception as e:
            print(f"Cursor Error: {e}")
            return False
        finally: cursor.close(); conn.close()