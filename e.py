def interest(n, x):
    t = 0.00
    for i in range(n):
        t += (x * (1 + (1/n))**n)
    return t

ans = interest(12, 1)
print("ans: ", ans)

def factorial(n):
    t = 1
    for i in range(n):
        t = t * (1 + i)
    print(t)
    return t

def euler_value(n):
    e = 0
    for i  in range(n+1):
        t = factorial(i)
        e += 1/t
    return e

e = euler_value(10)
print("e: ", e)
import math

a = math.e
print("a: ", a)