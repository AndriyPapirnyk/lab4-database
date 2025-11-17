from app.dao.user_account_dao import UserAccountDAO
from app.dtos.user_account_dto import UserAccountDTO

class UserAccountService:
    def __init__(self):
        self.dao = UserAccountDAO()

    def get_all(self):
        users = self.dao.get_all()
        return [u.to_dict() for u in users]

    def create(self, data):
        dto = UserAccountDTO(None, data['client_id'], data['username'], data['password_hash'], data['role'])
        return self.dao.create(dto)