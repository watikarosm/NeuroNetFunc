import numpy as np

# ActivationFunction using sigmoid
def sigmoid(x, y):
    y = 1/(1+np.exp(-x))
    return y

print(sigmoid(4, 3))