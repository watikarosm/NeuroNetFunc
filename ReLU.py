import numpy as np

def reLU(weightedInput):
    return np.max(weightedInput)

weightedInput = [0.95, 0.45, 0.55]
print("Weighted input (ReLU): highest value ", reLU(weightedInput), " from ", weightedInput)