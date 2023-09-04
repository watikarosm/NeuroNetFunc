import numpy as np
import math

# input, ie. dog, cat, human
layer_outputs = [4.8, 1.21, 2.385]
E = math.e
# exponentiate the inputs
exp_values = np.exp(layer_outputs)
# normalize the exponents
norm_values = exp_values / np.sum(exp_values)
# outputs
print(norm_values)
print(sum(norm_values))
