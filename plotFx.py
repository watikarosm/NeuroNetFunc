import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2 * x

def f1(x2):
    return (2 * pow(x2, 2))

def f2(x4):
    return (2 * pow(x4, 5))

x = [0, 1, 2, 3, 4]
x = np.array(range(5))
y = f(x)


print("x: ", x)
print("y: ", y)

x2 = y
x2 = np.arange(0, 50, 0.001)
y2 = f1(x2)

print("x2: ", x2)
print("y2: ", y2)

x4 = y2
x4 = np.arange(0, 25, 0.0001)
y4 = f2(x4)
print("x4: ", x4)
print("y4: ", y4)

colors = ['k', 'g', 'r', 'b', 'c']

def approximate_tangen_line(x1, approximate_derivative, b):
    return approximate_derivative * x1 + b

for i in range(5):
    p2_delta = 0.0001

    x1 = i
    x3 = x1 + p2_delta

    y1 = f1(x1)
    y3 = f1(x3)

    print((x1, y1), (x3, y3))

    approximate_derivative = (y3 - y1) / (x3 - x1)
    b = y3 - approximate_derivative * x3

    to_plot = [x1 - 0.9, x1, x1 + 0.9]
    plt.scatter(x1, y1, c=colors[i])
    plt.plot(to_plot, [approximate_tangen_line(point, approximate_derivative, b) 
                       for point in to_plot], c=colors[i])

    print('Approximate derivative for f(x2)', f'where x = {x1 is {approximate_derivative}}')

# plt.plot(x, y)

# plt.plot(x2, y2)

# plt.plot(x4, y4)
plt.show()