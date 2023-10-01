# https://www.youtube.com/watch?v=tMrbN67U9d4&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=3
# By sentdex

# 4 inputs, 1 neuron, 1 bias

import sys
import numpy as np
import matplotlib as mp

print("Python: ", sys.version)
print("Numpy: ", np.__version__)
print("Matplotlib: ", mp.__version__)

# inputs from sensors
a = 1.0
b = 2.0
c = 3.0
d = 4.0

def aNeuron(a, b, c, d):
    # ML variables
    inputs = [a, b, c, d]              # sensors or neurons
    weights = [0.66, 0.95, 0.01, 0.001]    # SD 
    bias = 3                        # single neuron == single bias

    output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
    print ("\nInside function output: ", output)
    return output

def threeNeurons(a, b, c, d):    # one layer
    # ML variables
    inputs = [a, b, c, d]              # sensors or neurons
    weight0 = [0.66, 0.95, 0.01, 0.001]    # SD 
    bias0 = 3                        # single neuron == single bias
    weight1 = [0.5, 0.99, 0.3, -0.75]    # SD 
    bias1 = 5                        # single neuron == single bias
    weight2 = [-0.4, -0.2, -0.85, 0.11]    # SD 
    bias2 = 7                        # single neuron == single bias

    output = [
        inputs[0]*weight0[0] + inputs[1]*weight0[1] + inputs[2]*weight0[2] + bias0,
        inputs[0]*weight1[0] + inputs[1]*weight1[1] + inputs[2]*weight1[2] + bias1,
        inputs[0]*weight2[0] + inputs[1]*weight2[1] + inputs[2]*weight2[2] + bias2,
    ]
    print ("\nInside function output: ", output)
    return output

cout1 = aNeuron(a, b, c, d)
cout3 = threeNeurons(a, b, c, d)
print("\n4 inputs, 1 neuron, 1 bias: ", cout1)
print("\n4 inputs, 3 neuron, 3 bias: ", cout3)

# Using cout1 and running it through threeNeuron function
coutAll = threeNeurons(cout1, cout1, cout1, cout1)
print("\n4 inputs, Using 1 neuron and running it through 3 neurons function: ", coutAll)

# Shape is the number of arrays that has number of elements
# shape (4) or (1, 4) == 1D array ==> l = [1, 2, 3, 4]
# shape (2, 4) == 2D array  ==> lol = [[1, 2, 3, 4], [1, 2, 3, 4]]
# shape (2, 2, 4) -- 3D array lolol = [[[1, 2, 3, 4], [1, 2, 3, 4]],[[1, 2, 3, 4], [1, 2, 3, 4]]]

def dotProduct(a, b, c, d):
    # inputs is just a vector while weights is a matrix and biases is also a vector
    inputs = [a, b, c, d]
    weights = [[0.66, 0.95, 0.01, 0.001],[0.5, 0.99, 0.3, -0.75],[-0.4, -0.2, -0.85, 0.11]]
    biases = [3, 5, 7]

    output = np.dot(weights, inputs) + biases   # weights come first, inputs second; plus, the biases
    # REMEMBER: dot product in linear algebra, larger matrix is multiplied by smaller matrix
    return output

coutDot = dotProduct(a, b, c, d)
print("\nDot product of the matrices: ", coutDot)

def batches(a, b, c, d):
    # inputs is a matrix and weights is also a matrix, which is [4 x 3] matrix, matrix multiplication
    # can be done only if first matrix's row elements is the same number of elements as the second matrix's column or less
    # Dot productable matrices are: [3 x 3].[3 x 3] or [2 x 3].[3 x 3]
    # |1, 2, 3|   |2, 3, 1|   |
    # |2, 1, 3| X |3, 1, 2| = |
    # |3, 1, 2|   |1, 2, 3|   |
    # Or
    # |1, 2, 3|   |2, 3, 1|   |2
    # |2, 1, 3| X |3, 1, 2| = |
    #             |1, 2, 3|   |
    inputs = [[a, b, c, d], [2.0, 5.0, -1.0, 2.0],[-1.5, 2.7, 3.3, -0.8]]
    weights = [[0.66, 0.95, 0.01, 0.001],[0.5, 0.99, 0.3, -0.75],[-0.4, -0.2, -0.85, 0.11]]
    biases = [3, 5, 7]

    output = np.dot(inputs, np.array(weights).T) + biases
    return output

coutBatch = batches(a, b, c, d)
print("\nOne layer with multiple batches of inputs: ")
print(coutBatch)

def twoLayersNeuron(a, b, c, d):
    inputs = [[a, b, c, d], [2.0, 5.0, -1.0, 2.0],[-1.5, 2.7, 3.3, -0.8]]
    weights = [[0.66, 0.95, 0.01, 0.001],[0.5, 0.99, 0.3, -0.75],[-0.4, -0.2, -0.85, 0.11]]
    biases = [3, 5, 7]

    weights1 = [[0.1, -0.14, 0.5], [-0.5, 0.12, -0.33], [-0.44, 0.73, -0.13]]
    biases1 = [-1, 2, -0.5]

    layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
    layer2_outputs = np.dot(layer1_outputs, np.array(weights1).T) + biases1
    return (layer2_outputs)

print("\nTwo-layer neurons: ")
print(twoLayersNeuron(a, b, c, d))

# Example of inputs, weights, and biases
inputs = [[a, b, c, d], [2.0, 5.0, -1.0, 2.0],[-1.5, 2.7, 3.3, -0.8]]
weights = [[0.66, 0.95, 0.01, 0.001],[0.5, 0.99, 0.3, -0.75],[-0.4, -0.2, -0.85, 0.11]]
biases = [3, 5, 7]
# using zip function
layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for each_input_set, weight in zip(inputs, neuron_weights):
        for each_input in each_input_set:
            neuron_output += (each_input * weight)
        # print("each_input ", each_input, " weight ", weight)
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print("layer_outputs reuslt using zip function: ", layer_outputs)
