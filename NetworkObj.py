# 3blue1brown
import numpy as np
import sigmoid as sig

class Network(obj):
    def __init__(self, *args, **kwargs):
        # initialize weights and biases...
        pass
    
    def feedForward(self, a): 
        # This is a single node that has all the math needed
        """Return the output of the network for an input vactor a """
        for b, w in zip(self.biases, self.weights):
            a = sig(np.dot(w, a)+b)
        return a