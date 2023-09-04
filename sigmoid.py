import numpy as np

def sigmoid(x, y):
    y = 1/(1+np.exp(-x))
    return y

print(sigmoid(4, 3))