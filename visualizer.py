import matplotlib.pyplot as plt
import numpy as np

def plot_pump_swapped_no_class(f_max, h_max, model, limit_bar):
    q = np.linspace(0, f_max * 1.1, 500) 
    h_pump = h_max * (1 - (q / f_max)**2)
    
    limit_m = limit_bar / 0.098
    mask = h_pump <= limit_m
    h_active = h_pump[mask]
    q_active = q[mask]
    # ----------------------------------

    plt.figure(figsize=(10, 6))
    plt.plot(h_active, q_active, label=f'Насос {model} (ВКЛ)', color='blue', lw=3)
    plt.axvline(x=limit_m, color='red', linestyle='--', label=f'Порог {limit_bar} bar')
    plt.title(f"Анализ работы {model} (Оси: Напор/Подача)", fontsize=14)
    plt.xlabel('Напор H (м)', fontsize=12) 
    plt.ylabel('Подача Q (м3/ч)', fontsize=12)
    
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.xlim(0, h_max * 1.1)
    plt.ylim(0, f_max * 1.1)
    plt.legend()
    
    plt.show()

