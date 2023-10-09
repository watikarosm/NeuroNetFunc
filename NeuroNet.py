import matplotlib.pyplot as plt
import numpy as np

weight00 = 0.95
weight01 = 0.75
weight10 = 0.50
weight11 = 0.25
bias0 = 0.50
bias1 = 0.25
colors = ['k', 'g', 'r', 'b', 'c']

np.random.seed(0)
def create_data(points):
    for point in range (points):
        point = np.random.randn(points)
    return point
X = create_data(100)
Y = create_data(100)

def yesORno(input0, input1):
    output0 = input0 * weight00 + input1 * weight01 + bias0
    output1 = input0 * weight10 + input1 * weight11 + bias1
    if(output0 > output1):
        return 1
    elif(output0 < output1):
        return 3
    else:
        print(" equal ")
        return 2
print("X = ", X, " Y = ", Y)
for i in X:
    for j in Y:
        print("(", i, ", ", j, ")")
        result = yesORno(i, j)
        print("result ", result)
    plt.scatter(i, j, c=colors[result])
    plt.plot(i, j, c=colors[result])


plt.show()
print("End")