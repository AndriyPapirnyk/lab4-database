class AccessLogDTO:
    def __init__(self, log_id, user_id, action, timestamp):
        self.log_id = log_id
        self.user_id = user_id
        self.action = action
        self.timestamp = str(timestamp) 

    def to_dict(self):
        return self.__dict__