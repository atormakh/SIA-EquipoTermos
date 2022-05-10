import numpy as np
def createTrainingSetWithNoise(trainingSet,probability):
    modify=lambda x: changeBooleanNumber(x) if np.random.random() < probability else x
    return np.vectorize(modify)(trainingSet)

def changeBooleanNumber(num):
    if(num == 0): return 1
    return 0