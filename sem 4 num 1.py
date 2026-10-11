import numpy as np
import matplotlib.pyplot as plt

a = np.array([38.0, 44.0, 42.0, 36.0, 33.0, 31.0, 29.0, 27.0, 25.0, 22.2]) / 100  # перевод см -> м
t = np.array([46.78, 47.92, 47.20, 46.20, 45.75, 45.51, 45.63, 45.73, 46.02, 46.67])  # время 30 колебаний
n = 30
T = t / n
sigma_a = 0.5e-3  
sigma_t = 0.2     
sigma_T = sigma_t / n
idx = np.argsort(a)
a_sort = a[idx]
T_sort = T[idx]

plt.figure(figsize=(8, 6), dpi=100)

plt.errorbar(a, T, xerr=sigma_a, yerr=sigma_T, fmt='.k', capsize=3, label='Экспериментальные точки')

plt.plot(a_sort, T_sort, '--r', linewidth=1)

plt.xlabel('$a$, м')
plt.ylabel('$T$, с')
plt.title('Рис. 1. Зависимость периода $T$ от положения призмы $a$')
plt.grid(True, linestyle='--')
plt.legend()

plt.show()