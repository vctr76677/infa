import tkinter as tk
import re

def calculate():
    s = expression.get()
    if not re.fullmatch(r'[0-9+\-*/%() ]+', s):
        result.config(text='Ошибка')
        return
    try:
        result.config(text='Ответ: ' + str(eval(s)))
    except (SyntaxError, ZeroDivisionError):
        result.config(text='Ошибка')

window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x180')

tk.Label(window, text='Введите выражение:').pack(pady=10)
expression = tk.Entry(window, width=35)
expression.pack()
tk.Button(window, text='Посчитать', command=calculate).pack(pady=10)
result = tk.Label(window, text='')
result.pack()

window.mainloop()
