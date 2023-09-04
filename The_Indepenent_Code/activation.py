import numpy as np
from layer import Layer
class Activation(Layer):
    def __init__(self, activation, derivative_of_activation):
        self.activation = activation
        self.derivative_of_activation = derivative_of_activation

    def forward(self, input):
        self.input = input
        return self.activation(self.input)
    
    def backward(self, output_gradient, learning_rate): # f'(x) = partial_derivative(Y) in respect to  partial_derivative(X)
        return np.multiply(output_gradient, self.derivative_of_activation(self.input))  # return multiplied element of both vectors
