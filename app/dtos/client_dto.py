class ClientDTO:
    def __init__(self, client_id, name, phone, email, fields=None):
        self.client_id = client_id
        self.name = name
        self.phone = phone
        self.email = email
        # Це поле для списку полів (Field), якщо ми їх завантажимо
        self.fields = fields if fields else []

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "fields": self.fields  # Додаємо зв'язані дані у вивід
        }