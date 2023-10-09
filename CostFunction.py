# Each node's cost function
def nodeCost(outputActivation, expectedOutput):
    errorValue = outputActivation - expectedOutput
    return errorValue * errorValue

outputActivation = 0.75
expectedOutput = 0.95
print("Each neuron's cost (error) function: ", nodeCost(outputActivation, expectedOutput))

'''
def singleCost(singleDataPoint):
    outputs[] = calculatedOutputs(singleDataPoint.inputs)
    outputLayer = layers[len(layers) - 1]
    for i in outputs:
        cost += outputLayer.nodeCost(outputs[i], singleDataPoint.expectedOutputs[i])
    return Cost

def overallCost(allDataPoints):
    totalCost = 0
    for i in allDataPoints:
        totalCost += sigleCost(i)
    return totalCost / len(allDataPoints)
'''