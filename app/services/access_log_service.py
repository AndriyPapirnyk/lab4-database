from app.dao.access_log_dao import AccessLogDAO
from app.dtos.access_log_dto import AccessLogDTO
from datetime import datetime

class AccessLogService:
    def __init__(self):
        self.dao = AccessLogDAO()

    # READ ALL
    def get_all(self):
        logs = self.dao.get_all()
        return [l.to_dict() for l in logs]
        
    # READ BY ID
    def get_by_id(self, log_id):
        log = self.dao.get_by_id(log_id)
        return log.to_dict() if log else None

    # CREATE
    def create(self, data):
        # Якщо timestamp не передали, беремо поточний час
        ts = data.get('timestamp', datetime.now())
        dto = AccessLogDTO(None, data['user_id'], data['action'], ts)
        return self.dao.create(dto)

    # UPDATE
    def update(self, log_id, data):
        return self.dao.update(log_id, data)

    # DELETE
    def delete(self, log_id):
        return self.dao.delete(log_id)