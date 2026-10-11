import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

df_iris = pd.read_csv('iris_data.csv')

features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
pairs = list(combinations(features, 2))  # Получаем ровно 6 пар

fig, axes = plt.subplots(2, 3, figsize=(15, 9))
axes = axes.flatten()

for i, (f1, f2) in enumerate(pairs):
    x = df_iris[f1]
    y = df_iris[f2]
    
    axes[i].scatter(x, y, alpha=0.7, color='teal', edgecolors='k', s=30)
    axes[i].set_xlabel(f1)
    axes[i].set_ylabel(f2)
    axes[i].grid(True, linestyle='--', alpha=0.5)
    
    # Прямая МНК (линейная регрессия y = k*x + b)
    k, b = np.polyfit(x, y, 1)
    x_range = np.linspace(x.min(), x.max(), 100)
    axes[i].plot(x_range, k * x_range + b, color='red', linestyle='--', label=f'МНК: y={k:.2f}x+{b:.2f}')
    axes[i].legend(fontsize=8)

plt.suptitle('Все пары признаков Ирисов с прямыми МНК', fontsize=14)
plt.tight_layout()
plt.show()

