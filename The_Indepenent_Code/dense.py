from layer import Layer
import numpy as np

# Step 2: Create the base layer

# Step 3: Create Dense layer
class Dense(Layer):
    def __init__(self, input_size, output_size):    # constructor
        self.weights = np. random.randn(output_size, input_size)
        self.bias = np.random.randn(output_size, 1)

    def forward(self, input):   # Y = X*W + B
        self.input = input
        return np.dot(self.weights, self.input) + self.bias
    
    def backward(self, output_gradient, learning_rate):
        weights_gradient = np.dot(output_gradient, self.input.T)    # weights_gradient: partial_derivative(E) in respect to  partial_derivative(W) = partial_derivative(E) in respect to  partial_derivative(Y) * Transpose(X)
        self.weights -= learning_rate * weights_gradient    # output_gradient: partial_derivative(E) in respect to  partial_derivative(B) = partial_derivative(E) in respect to  partial_derivative(Y)
        self.bias -= learning_rate *output_gradient
        return np.dot(self.weights.T, output_gradient)  # return the derivative of the error: weights_gradient: partial_derivative(E) in respect to  partial_derivative(X) =  Transpose(W) * partial_derivative(E) in respect to  partial_derivative(Y)

# class Dense_Layer outline:
    # y1, x1, w11, x2, w12, xi, wii, b1, b2, b3, bi = 0
    # Y, W, X, B = 0
    # y1 = x1*w11 + x2*w12 + ... + xi*w1i + b1
    # y2 = x2*w22 + x2*w22 + ... + xi*w2i + b2
    # y3 = x2*w32 + x2*w32 + ... + xi*w3i + b3
    # yi = x2*wi2 + x2*wi2 + ... + xi*wii + bi
    # Y = W * X + B
