#import numpy as np

def pressure(f, a):
    p = f/a
    print("Pressure: ", p, " force exerts: ", f, " area to apply: ", a)
    return p

p = pressure(4, 2)
print("p = ", p)

def energy(m):
    c = 299792458
    print("Speed of light is measured in meter per second: ", c, "m/s")

    e = m*c*c
    print("energy: ", e, " mass: ", m, " speed of light: ", c)
    return e

m = 2
e = energy(m)
print("Energy of ", e, " is released for the mass of ", m, " is used.")