import numpy as np
def createTrainingSetWithNoise(trainingSet):
    modify=lambda x: changeBooleanNumber(x) if np.random.random() < 0.22 else x
    return np.vectorize(modify)(trainingSet)

def changeBooleanNumber(num):
    if(num == 0): return 1
    return 0