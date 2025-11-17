class UserAccountDTO:
    def __init__(self, user_id, client_id, username, password_hash, role):
        self.user_id = user_id
        self.client_id = client_id
        self.username = username
        self.password_hash = password_hash
        self.role = role
    def to_dict(self):
        return self.__dict__