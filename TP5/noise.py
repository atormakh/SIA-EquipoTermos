import numpy as np
def addNoise(trainingSet,probability,noiseRange):
    modify=lambda x: changeNumber(x,noiseRange) if np.random.random() < probability else x
    return np.vectorize(modify)(trainingSet.copy())

def changeNumber(num,noiseRange):
    noiseNum = np.random.uniform(0,noiseRange)
    if(num==0):
        return num + noiseNum
    return num - noiseNum