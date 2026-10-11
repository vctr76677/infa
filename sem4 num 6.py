import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_btc = pd.read_csv('BTC_data.csv')
df_btc['time'] = pd.to_datetime(df_btc['time'])
df_btc = df_btc.sort_values('time').reset_index(drop=True)

# Для polyfit переводим время в обычный числовой массив индексов [0, 1, 2, ..., N-1]
x_nums = np.arange(len(df_btc))
y_prices = df_btc['close'].values

# Считаем коэффициенты полинома (например, 3-й и 6-й степени)
coeffs_3 = np.polyfit(x_nums, y_prices, 3)
poly_3 = np.poly1d(coeffs_3)

coeffs_6 = np.polyfit(x_nums, y_prices, 6)
poly_6 = np.poly1d(coeffs_6)

plt.figure(figsize=(13, 6))

# Исходный график цены
plt.plot(df_btc['time'], y_prices, color='gray', alpha=0.6, label='Реальная цена close')

# Графики полиномов
plt.plot(df_btc['time'], poly_3(x_nums), color='blue', linewidth=2, label='Полином 3-й степени')
plt.plot(df_btc['time'], poly_6(x_nums), color='crimson', linewidth=2, linestyle='--', label='Полином 6-й степени')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

plt.xticks(rotation=45)
plt.xlabel('Дата (DD-MM-YY)')
plt.ylabel('Цена (USD)')
plt.title('Аппроксимация цены BTC полиномами')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

print("Полученный полином 3-й степени:")
print(poly_3)