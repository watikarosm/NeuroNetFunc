import numpy as np

def siLU(weightedInput):
    return weightedInput / (1 + np.exp(-weightedInput))

weightedInput = 0.95
print("Weighted Input (SiLU): ", siLU(weightedInput))