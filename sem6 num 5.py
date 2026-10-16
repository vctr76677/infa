
import tkinter as tk
import random

def create_ball(event):
    x = event.x
    y = event.y
    r = 20
    color = f'#{random.randint(0, 0xffffff):06x}'
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=color)

window = tk.Tk()
window.title('Шарики')

canvas = tk.Canvas(window, width=500, height=400, bg='white')
canvas.pack()
canvas.bind('<Button-1>', create_ball)

window.mainloop()
