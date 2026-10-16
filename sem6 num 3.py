
import tkinter as tk
import pandas as pd

films = pd.read_csv('imdb_top_250.csv')

def find_movie():
    genre = genre_entry.get().strip().lower()
    if not genre:
        result.config(text='Введите жанр')
        return

    selected = films[films['Genre'].fillna('').apply(
        lambda s: genre in [g.strip().lower() for g in s.split('|')]
    )]
    movie = selected.sample(1).iloc[0]
    result.config(text=str(movie['Title']))

window = tk.Tk()
window.title('Фильмотека')
window.geometry('450x200')

tk.Label(window, text='Введите жанр фильма:').pack(pady=10)
genre_entry = tk.Entry(window, width=30)
genre_entry.pack()

tk.Button(window, text='Найти фильм', command=find_movie).pack(pady=10)
result = tk.Label(window, text='', wraplength=420)
result.pack()

window.mainloop()
