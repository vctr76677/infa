import pandas as pd
import matplotlib.pyplot as plt

df_iris = pd.read_csv('iris_data.csv')
fig, axes = plt.subplots(1, 2, figsize=(13, 6))

species_counts = df_iris['Species'].value_counts()
axes[0].pie(
    species_counts, 
    labels=species_counts.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#ff9999','#66b3ff','#99ff99']
)
axes[0].set_title('Доля видов ирисов (Species)')


p_len = df_iris['PetalLengthCm']
count_less_12 = (p_len < 1.2).sum()
count_12_to_15 = ((p_len >= 1.2) & (p_len <= 1.5)).sum()
count_more_15 = (p_len > 1.5).sum()

counts_petal = [count_less_12, count_12_to_15, count_more_15]
labels_petal = [' < 1.2 см', '1.2 см ≤ ≤ 1.5 см', ' > 1.5 см']

axes[1].pie(
    counts_petal, 
    labels=labels_petal, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#c2c2f0','#ffb3e6','#ffcc99']
)
axes[1].set_title('Доли ирисов по длине лепестка')

plt.tight_layout()
plt.show()