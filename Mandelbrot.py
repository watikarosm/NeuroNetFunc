# Mandelbrot function: returns a value between 0 and 1 based on the Mandelbrot set, where 1 is in the set and <1 is not in the set.  The closer the value is to 1, the more iterations it took to determine that it was not in the set.
import numpy as np

x = [-2.5, 1]
y = [-1.1, 1.1]

def mandelbrot(x, y):
    a = x + 1j * y
    max_depth = 100
    z = 0
    for iteration in range(max_depth):
        z = z**2 + a
        if abs(z) > 2:
            return 1-(1/((iteration/50) + 1))   # this smooths out the value in range [o, 1)
    return 1.0


output = np.array[mandelbrot(x, y)]
print(output)