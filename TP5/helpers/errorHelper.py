import math
import numpy as np

class ErrorHelper:

    def __init__(self,trainingSet,resultsSet,layers):
        self.trainingSet = trainingSet
        self.resultsSet = resultsSet
        self.layers = layers
    
    # # X = (W0, W1, W2, w11, w12, w13, w21, w22, w23, , w01, w02)

    # def f(self,genes,epsilon):
    #     #Modelamos los genes del individuo como los arrays y matrices mostrados en el enunciado
    #     W = np.array(genes[0:3])
    #     w = np.array([genes[3:6],genes[6:9]])
    #     w0 = np.array(genes[9:11])

    #     (rowsCount, columsCount) = w.shape

    #     #Calculamos la funcion F
        
    #     totalAcum = 0

    #     for j in range(0,rowsCount):
    #         colAcum = 0
    #         for k in range(0,columsCount):
    #             colAcum+=(w[j][k]*epsilon[k])
    #         totalAcum += (W[j]*self.g(colAcum-w0[j]))
    #     return self.g(totalAcum - W[0])

    # def g(self,x):
    #     try:
    #         return math.exp(x)/(1+math.exp(x))
    #     except:
    #         return 1

    def error(self,weightsFlattened,step=None):
        outputArray = []
        for trainingArray in self.trainingSet:
            inputs = np.matrix(trainingArray).transpose()
            #propagate
            for layer in self.layers:
                output= layer.propagate(inputs)
                inputs=output
            outputArray.append(inputs)
        #print("Result Set =",str(resultsSet), "outputSet", str(outputSet))
        error=0
        pow = lambda x: x**2
        for i in range(0,len(self.resultsSet)):
            diff=self.resultsSet[i]-outputArray[i]
            error+=0.5*np.sum(np.vectorize(pow)(diff))
        return  error/len(self.resultsSet)
        