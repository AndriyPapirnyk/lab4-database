class SprinklerDTO:
    def __init__(self, sprinkler_id, field_id, gps_id, max_flow):
        self.sprinkler_id = sprinkler_id
        self.field_id = field_id
        self.gps_id = gps_id
        self.max_flow = float(max_flow)
    def to_dict(self):
        return self.__dict__