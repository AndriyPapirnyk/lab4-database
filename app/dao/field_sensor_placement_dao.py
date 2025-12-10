from app.db_config import get_db_connection
from app.dtos.field_sensor_placement_dto import FieldSensorPlacementDTO

class FieldSensorPlacementDAO:
    
    def get_all(self):
        conn = get_db_connection(); cursor = conn.cursor(dictionary=True)
        
        sql = """
            SELECT 
                P.field_id, 
                P.sensor_id, 
                P.placement_date, 
                S.type AS sensor_type, 
                S.model AS sensor_model 
            FROM Field_Sensor_Placement P
            JOIN Sensor S ON P.sensor_id = S.sensor_id
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        placements = []
        for r in rows:
            sensor_details = {
                "id": r['sensor_id'],
                "type": r['sensor_type'],
                "model": r['sensor_model']
            }
            
            dto = FieldSensorPlacementDTO(
                r['field_id'], 
                r['sensor_id'], 
                r['placement_date'], 
                sensor_details=sensor_details
            )
            placements.append(dto)

        cursor.close(); conn.close()
        return placements
    
    # 2.b. Процедура: Зв'язок за назвами
    def create_by_names(self, field_name, sensor_model):
        conn = get_db_connection(); cursor = conn.cursor()
        try:
            cursor.callproc('PlaceSensorByName', [field_name, sensor_model])
            conn.commit()
            return True
        except Exception as e:
            print(f"Procedure M:M Error: {e}")
            return False
        finally: cursor.close(); conn.close()
        
