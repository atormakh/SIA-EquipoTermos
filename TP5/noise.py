import numpy as np
def addNoise(trainingSet,probability):
    modify=lambda x: changeNumber(x) if np.random.random() < probability else x
    return np.vectorize(modify)(trainingSet.copy())

def changeNumber(num):
    # return num + np.random.normal(0,1)
    if(num == 0): return 1
    return 0