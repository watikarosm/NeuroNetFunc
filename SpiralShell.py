import numpy as np

# Parameters that control the shell shape
r = 1
a = 1.25
b = 1.25
c = 1
d = 3.5
e = 0
f = 0.17
h = -1

# Parametric surface function:
def spiralShell(u, v):
    exp = pow(np.e, f*v)
    x = r*exp * (-1.4*e + b*np.sin(v))
    y = r*exp * (d + a*np.cos(v)) * np.sin(c*u)
    z = r*exp * (d + a*np.cos(v)) * np.cos(c*u) + h
    return np.array([x, y, z])

print(spiralShell(4, 5))