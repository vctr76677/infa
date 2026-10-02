import numpy as np

N, M = map(int, input().split())

a = np.zeros((N, M), dtype=int)
x, y = 0, 0
dx, dy = 0, 1
for val in range(1, N * M + 1):
    a[x][y] = val
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < M and a[nx][ny] == 0:
        x, y = nx, ny
    else:
        if dx == 0 and dy == 1:
            dx, dy = 1, 0
        elif dx == 1 and dy == 0:
            dx, dy = 0, -1
        elif dx == 0 and dy == -1:
            dx, dy = -1, 0
        elif dx == -1 and dy == 0:
            dx, dy = 0, 1
        x += dx
        y += dy
for i in range(N):
    a[i] = a[i] * i
print(a)