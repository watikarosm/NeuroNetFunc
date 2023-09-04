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

class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_Categorical_Cross_entropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods