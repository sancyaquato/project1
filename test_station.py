import pytest
from models import CentrifugalPump, PressureSensor

def test_pump_math():
    p = CentrifugalPump("Test", 100, 50, 10, 3000)
    assert p.get_characteristic(0) == 50
    assert p.get_characteristic(100) == 0

def test_sensor_alarm():
    s = PressureSensor("S1", 2.0)
    res = s.read_pressure(3.76) 
    assert res["status"] == "Ошибка"

def test_json_structure():
    s = PressureSensor("S1", 5.0)
    res = s.read_pressure(10)
    assert "value" in res and "status" in res

def test_overheat_shutdown():
    from models import CentrifugalPump, TempSensor
    pump = CentrifugalPump("Test", 50, 40, 5, 2900)
    t_sensor = TempSensor("T1", max_temp=60)
    
def test_emergency_shutdown_logic():
    pump = CentrifugalPump("TestPump", 50, 40, 5, 2900)
    sensor = PressureSensor("PS-01", 2.0) 

   
    head = pump.get_characteristic(0) 
    p_data = sensor.read_pressure(head) 
    
    if p_data["status"] == "Ошибка":
        pump.set_speed(0)

    assert pump.current_speed == 0
    assert p_data["status"] == "Ошибка"