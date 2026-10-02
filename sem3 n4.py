def draw_triangle(size, symb):
    for i in range(1, size + 1):
        print(symb * i)

# Пример ввода: 7 c
data = input().split()
draw_triangle(int(data[0]), data[1])