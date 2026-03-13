from models import CentrifugalPump, PressureSensor
from data_manager import save_to_json, save_to_csv
from visualizer import plot_pump_swapped_no_class 

def main():
    pump = CentrifugalPump("CP-100", 50, 40, 5.5, 2900)
    sensor = PressureSensor("PS-01", 3.0) 
    
    results = []
    for q in [10, 20, 30, 40, 50]:
        h = pump.get_characteristic(q)
        p_data = sensor.read_pressure(h)
        record = {"flow": q, "head": round(h, 2), **p_data}
        results.append(record)
        
        if p_data["status"] == "Ошибка":
            print(f"АВАРИЯ: Давление {p_data['value']} bar превышено!")
            pump.set_speed(0) # Теперь это ВНУТРИ if
            print("Система безопасности: Насос остановлен.") 

    save_to_json(results)
    save_to_csv(results)
    print("Данные сохранены в JSON и CSV")

plot_pump_swapped_no_class (50, 40, "CP-100", 3.76)

if __name__ == "__main__":
    main()