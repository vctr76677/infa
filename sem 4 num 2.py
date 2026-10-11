import numpy as np
import matplotlib.pyplot as plt
kolvo= [100, 1000, 10000, 100000]

fig, axes = plt.subplots(2, 2, figsize=(11, 8))
axes = axes.flatten()
x_th = np.linspace(-4, 4, 300)
y_th = (1 / np.sqrt(2 * np.pi)) * np.exp(-x_th**2 / 2)

for i, n in enumerate(kolvo):
    # Генерация N точек из N(0, 1)
    data = np.random.normal(loc=0, scale=1, size=n)
    
    # Строим гистограмму
    axes[i].hist(data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
    axes[i].plot(x_th, y_th, 'r--', linewidth=2)
    
    axes[i].set_title(f'N = {n} точек')
    axes[i].set_xlabel('Значение')
    axes[i].set_ylabel('Плотность')
    axes[i].grid(True, linestyle='--', alpha=0.5)
    axes[i].legend()

plt.suptitle('Стремление гистограммы выборочных значений к нормальному распределению', fontsize=13)
plt.tight_layout()
plt.show()