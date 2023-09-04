''' Create a random dataset '''

import numpy as np
np.random.seed(0)
# for testing only
def vertical_data(points, classes):
    X = np.zeros((points * classes, 2))
    y = np.zeros(points * classes, dtype='uint8')
    for class_number in range (classes):
        ix = range(points * class_number, points * (class_number+1))
        r = np.linspace(0.0, 1, points) #radius
        t = np.linspace(class_number + 1 * 4, (class_number + 1) * 4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r, t]
        y[ix] = class_number
    return X, y
X, y = vertical_data(100, 3)
''' END Create a random dataset '''
''' --------------------------- '''


''' Graph '''
import matplotlib.pyplot as plt
import MLobj_1 as ml

densel = ml.Layer_Dense(2, 3)
activation1 = ml.Activation_ReLU()
dense2 = ml.Layer_Dense(3, 3)
activation2 = ml.Activation_Softmax()

loss_function = ml.Loss_Categorical_Cross_entropy()

lowest_loss = 9999999

best_dense1_weights = densel.weights.copy()
best_dense1_biases = densel.biases.copy()
best_dense2_weights = dense2.weights.copy()
bes_dense2_biases = dense2.biases.copy()

for iteration in range(100000):
    densel.weights += 0.05 * np.random.randn(2, 3)
    densel.biases += 0.05 * np.random.randn(1, 3)
    dense2.weights += 0.05 * np.random.randn(3, 3)
    dense2.biases += 0.05 * np.random.randn(1, 3)
    densel.forward(X)
    activation1.forward(densel.output)
    dense2.forward(activation1.output)
    activation2.forward(dense2.output)
    loss = loss_function.calculate(activation2.output, y)
    predictions = np.argmax(activation2.output, axis=1)
    accuracy = np.mean(predictions==y)
    if loss < lowest_loss:
        print('New set of weights found, iteration: ', iteration, 'loss: ', loss, 'accuracy: ', accuracy)
        best_dense1_weights = densel.weights.copy()
        best_dense1_biases = densel.biases.copy()
        best_dense2_weights = dense2.biases.copy()
        bes_dense2_biases = dense2.biases.copy()
        lowest_loss = loss



plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap='brg')
plt.show()
