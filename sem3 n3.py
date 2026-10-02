def gcd_ext(a, b):
    if a == 0:
        return 0, 1, b
    x1, y1, d = gcd_ext(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return x, y, d

def solve(a, b):
    x, y, d = gcd_ext(a, b)
    
    dx = b // d
    dy = a // d
    
    best_x = x
    best_y = y
    min_sum = abs(x) + abs(y)
    
    for k in range(-100, 101):
        nx = x + k * dx
        ny = y - k * dy
        s = abs(nx) + abs(ny)
        if s < min_sum:
            min_sum = s
            best_x = nx
            best_y = ny
        elif s == min_sum and nx < best_x:
            best_x = nx
            best_y = ny
            
    return best_x, best_y, d

while True:
    try:
        line = input()
        if not line:
            break
        a, b = map(int, line.split())
        res_x, res_y, res_d = solve(a, b)
        print(f"{res_x} {res_y} {res_d}")
    except EOFError:
        break