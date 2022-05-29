import numpy as np

def getWeights(dimension):
    w = []
    for i in range(0,dimension):
        w.append(np.random.uniform(-1,1))
    return np.array(w)

def applyOja(epochs,data,w,learningRate):
    dataRows = data.shape[0]
    for k in range(0,epochs):
        for i in range(0,dataRows):
            row = np.array(data[i])
            s = np.dot(row,w)
            deltaW = np.multiply(learningRate*s,np.subtract(row,np.multiply(s,w)))
            w = np.add(w,deltaW)
    return w