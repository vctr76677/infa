import numpy as np

def mnk(x, y):
    x = np.array(x)
    y = np.array(y)
    
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    k = (np.mean(x * y) - x_mean * y_mean) / (np.mean(x2) - x_mean2)
    b = y_mean - k * x_mean
    
    return k, b