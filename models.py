import numpy as np

class CentrifugalPump:
    def __init__(self, model, flow_max, head_max, power, speed_nominal):
        self.model = model
        self.flow_max = flow_max
        self.head_max = head_max
        self.power = power
        self.speed_nominal = speed_nominal 
        self.current_speed = speed_nominal

    @property
    def hydraulic_power(self):
        return (1000 * 9.81 * self.flow_max * self.head_max) / 3600000

    def get_characteristic(self, flow):
        speed_ratio = (self.current_speed / self.speed_nominal)**2
        head = self.head_max * (1 - (flow / self.flow_max)**2) * speed_ratio
        return max(0, head)

    def set_speed(self, speed):
        self.current_speed = speed

class PressureSensor:
    def __init__(self, sensor_id, range_max):
        self.id = sensor_id
        self.range_max = range_max

    def read_pressure(self, current_head):
        pressure = round(current_head * 0.098, 2)
        status = "OK" if pressure <= self.range_max else "Ошибка"
        return {"value": pressure, "unit": "bar", "status": status}
