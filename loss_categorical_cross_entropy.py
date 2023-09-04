import numpy as np
import math
'''
Refresh on log:
b = 2
print(np.log(b))
print(math.e **1)
'''
label = 3
one_hot = [1, 0, 0]
prediction = [0.7, 0.1, 0.2]        # aka softmax_output


''' Lost Function '''
def loss_func(one_hot, prediction):
    L = 0
    for i in range(len(one_hot)):
        L += (one_hot[i] * math.log(prediction[i]))
        # print(one_hot[i], " prediction: ", prediction[i], " ", L)
        L = L * (-1)
    # print("total ", L)
    return L

'''
Here's the fun part...
'''

softmax_output = [0.7, 0.1, 0.2]
target_output = [1, 0, 0]
loss = loss_func(one_hot, prediction)
print(loss)