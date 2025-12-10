from app.dao.client_dao import ClientDAO
from app.dtos.client_dto import ClientDTO

class ClientService:
    def __init__(self):
        self.dao = ClientDAO()

    def get_all_clients(self):
        clients = self.dao.get_all()
        return [client.to_dict() for client in clients]

    def get_by_id(self, client_id):
        client = self.dao.get_by_id(client_id)
        return client.to_dict() if client else None

    def create_client(self, data):
        if '@' not in data.get('email', ''):
            return False
            
        new_client = ClientDTO(None, data['name'], data['phone'], data['email'])
        return self.dao.create(new_client)

    def update_client(self, client_id, data):
        return self.dao.update(client_id, data)

    def delete_client(self, client_id):
        return self.dao.delete(client_id)

    def get_client_details(self, client_id):
        client = self.dao.get_client_with_fields(client_id)
        if client:
            return client.to_dict()
        return None