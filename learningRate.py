import numpy as np

startAt = 0
learningRate = 0

def someFunction(x):
    return (0.2 * np.power(x, 4) + 0.1 * np.power(x, 3)- np.power(x, 2) +2)

def startingPoint(randomValue):
    np.random.seed(0)
    startAt = np.random.rand(randomValue)
    return startAt

def learning(learningRate, startAt):
    h = 0.0001
    inputValue = 0
    deltaOutput = someFunction(startAt + h) - someFunction(startAt)
    slope = deltaOutput / h
    inputValue -= slope * learningRate
    return inputValue

startAt = startingPoint(3)

print(startAt)
print(learning(2, startAt))