#import math

def multiplication(a, b, c):
    c = b * a
    return c

def division(a, b, c):
    c = b / a
    return c

def mach(M, V, a):
    M = V / a
    return M

def gasLaw(p, ro, T):
    pressure = p
    temperature = T
    density = ro
    ratio_heat_specific = (7/5)
    pressure = density * ratio_heat_specific * temperature
    return pressure



