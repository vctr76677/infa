import numpy as np

def solve_system():
    n, m = map(int, input().split())
    data = []
    for _ in range(n):
        row = list(map(float, input().split()))
        data.append(row)
    
    mat = np.array(data)
    A = mat[:, :-1]
    b = mat[:, -1]
    
    try:
        ans = np.linalg.solve(A, b)
    except:
        ans = np.linalg.lstsq(A, b, rcond=None)[0]
        
    return ans

print(solve_system())