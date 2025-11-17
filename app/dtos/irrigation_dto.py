class IrrigationDTO:
    def __init__(self, irrigation_id, pump_id, start_time, end_time, flow_rate, duration_minutes=0, total_volume=0.0):
        self.irrigation_id = irrigation_id
        self.pump_id = pump_id
        self.start_time = str(start_time)
        self.end_time = str(end_time)
        self.flow_rate = float(flow_rate)
        # Ці поля обчислюються БД, тому при створенні можуть бути None/0
        self.duration_minutes = duration_minutes 
        self.total_volume = float(total_volume) if total_volume else 0.0
    def to_dict(self):
        return self.__dict__