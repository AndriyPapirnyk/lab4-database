class PumpDTO:
    def __init__(self, pump_id, field_id, model, max_flow):
        self.pump_id = pump_id
        self.field_id = field_id
        self.model = model
        self.max_flow = float(max_flow)
    def to_dict(self):
        return self.__dict__