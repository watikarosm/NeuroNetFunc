import numpy as np

np.random.seed(0)

X = [[1, 2, 3, 2.5], [2.0, 5.0, -1.0, 2.0],[-1.5, 2.7, 3.3, -0.8]]
inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
output = []

# A simple step function
# 
# for i in inputs:
#     if i > 0:
#         output.append(i)
#     elif i <= 0:
#         output.append(0)
# Or
for i in inputs:
    output.append(max(0, i))
    
print(output)