from app.dao.access_log_dao import AccessLogDAO
from app.dtos.access_log_dto import AccessLogDTO
from datetime import datetime

class AccessLogService:
    def __init__(self):
        self.dao = AccessLogDAO()

    def get_all(self):
        logs = self.dao.get_all()
        return [l.to_dict() for l in logs]

    def create(self, data):
        # Якщо timestamp не передали, беремо поточний час
        ts = data.get('timestamp', datetime.now())
        dto = AccessLogDTO(None, data['user_id'], data['action'], ts)
        return self.dao.create(dto)