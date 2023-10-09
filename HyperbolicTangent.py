import numpy as np

def hyperbolicTangent(weightedInput):
    e2w = np.exp(2 * weightedInput)
    return (e2w - 1) / (e2w +1)

weightedInput = 0.95
print("Weighted input (hyperbolic tangent) : ", hyperbolicTangent( weightedInput))