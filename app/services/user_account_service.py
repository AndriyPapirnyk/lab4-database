from app.dao.user_account_dao import UserAccountDAO
from app.dtos.user_account_dto import UserAccountDTO

class UserAccountService:
    def __init__(self):
        self.dao = UserAccountDAO()

    # READ ALL
    def get_all(self):
        users = self.dao.get_all()
        return [u.to_dict() for u in users]
        
    # READ BY ID
    def get_by_id(self, user_id):
        user = self.dao.get_by_id(user_id)
        return user.to_dict() if user else None

    # CREATE
    def create(self, data):
        dto = UserAccountDTO(None, data['client_id'], data['username'], data['password_hash'], data['role'])
        return self.dao.create(dto)

    # UPDATE
    def update(self, user_id, data):
        return self.dao.update(user_id, data)

    # DELETE
    def delete(self, user_id):
        return self.dao.delete(user_id)