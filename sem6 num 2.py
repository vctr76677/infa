import tkinter as tk

def calculate():
    try:
        weight = float(weight_entry.get().replace(',', '.'))
        height = float(height_entry.get().replace(',', '.')) / 100
        if weight <= 0 or height <= 0:
            raise ValueError
        bmi = weight / height ** 2

        if bmi < 16:
            text = 'Выраженный дефицит массы тела'
        elif bmi < 18.5:
            text = 'Недостаточная масса тела'
        elif bmi < 25:
            text = 'Нормальная масса тела'
        elif bmi < 30:
            text = 'Избыточная масса тела'
        elif bmi < 35:
            text = 'Ожирение I степени'
        elif bmi < 40:
            text = 'Ожирение II степени'
        else:
            text = 'Ожирение III степени'

        result.config(text=f'ИМТ: {bmi:.2f}\n{text}')
    except ValueError:
        result.config(text='Введите правильные данные')

window = tk.Tk()
window.title('Индекс массы тела')
window.geometry('350x260')

tk.Label(window, text='Вес (кг):').pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text='Рост (см):').pack(pady=5)
height_entry = tk.Entry(window)
height_entry.pack()

tk.Button(window, text='Рассчитать', command=calculate).pack(pady=15)
result = tk.Label(window, text='')
result.pack()

window.mainloop()
