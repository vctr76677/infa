import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Загружаем данные по BTC
df_btc = pd.read_csv('BTC_data.csv')

# Преобразуем строковые даты в формат datetime
df_btc['time'] = pd.to_datetime(df_btc['time'])

# На всякий случай отсортируем по возрастанию даты
df_btc = df_btc.sort_values('time').reset_index(drop=True)

plt.figure(figsize=(12, 6))
plt.plot(df_btc['time'], df_btc['close'], color='darkorange', linewidth=1.5, label='BTC Close Price')

# Настраиваем формат зарубок на оси X: DD-MM-YY
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

plt.xticks(rotation=45)
plt.xlabel('Дата (DD-MM-YY)')
plt.ylabel('Цена закрытия (USD)')
plt.title('Исторический график цены биткоина (BTC)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()