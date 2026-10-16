
import tkinter as tk

def find_color():
    color = entry.get().strip()
    try:
        if len(color) != 7 or color[0] != '#':
            raise ValueError
        r = 255 - int(color[1:3], 16)
        g = 255 - int(color[3:5], 16)
        b = 255 - int(color[5:7], 16)
        new_color = f'#{r:02x}{g:02x}{b:02x}'
        answer.config(text=new_color)
        first.config(bg=color)
        second.config(bg=new_color)
    except ValueError:
        answer.config(text='Неверный цвет')

window = tk.Tk()
window.title('Подбор цветов')
window.geometry('350x230')

tk.Label(window, text='Введите цвет в формате #RRGGBB').pack(pady=10)
entry = tk.Entry(window)
entry.pack()

tk.Button(window, text='Подобрать цвет', command=find_color).pack(pady=10)
answer = tk.Label(window, text='')
answer.pack()

first = tk.Label(window, width=15, height=3, bg='white')
first.pack(side='left', padx=20)
second = tk.Label(window, width=15, height=3, bg='white')
second.pack(side='right', padx=20)

window.mainloop()
