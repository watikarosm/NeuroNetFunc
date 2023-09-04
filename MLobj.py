import numpy as np
np.random.seed(0)
def create_data(points, classes):
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range (classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points) #radius
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y
X, y = create_data(100, 3)
# X = [[1, 2, 3, 2.5], [2.0, 5.0, -1.0, 2.0],[-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__ (self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)       #parameters are the shape
        self.biases = np.zeros((1, n_neurons))    # shape is the first parameter
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class Activatin_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities


# layer1 = Layer_Dense(4, 5)
# activation1 = Activation_ReLU()
# layer2 = Layer_Dense(5, 2)
# activation2 = Activation_ReLU()
# layer3 = Layer_Dense(2, 7)
# activation3 = Activation_ReLU()

# Layer1
# layer1.forward(X)
# activation1.forward(layer1.output)
# print("\nLayer1: ")
# print(layer1.output)
# print("ReLU Act1: \n", activation1.output)

# # Layer 2
# layer2.forward(activation1.output)
# print("\nLayer2: ")
# print(layer2.output)
# activation2.forward(layer2.output)
# print("ReLU Act2: \n", activation2.output)

# # Layer 3
# layer3.forward(activation2.output)
# print("\nLayer3: ")
# print(layer3.output)
# activation3.forward(layer3.output)
# print("ReLU Act3: \n", activation3.output)

# # random function for data creation
# print("\nRandom matrix: ")
# print(np.random.randn(4, 3))