import math
import numpy as np

class ErrorHelper:

    def __init__(self,trainingSet,resultsSet,layers):
        self.trainingSet = trainingSet
        self.resultsSet = resultsSet
        self.layers = layers

    def error(self,weightsFlattened,step=None):
        outputArray = []
        #Actualizamos los pesos de las layers
        self.updateLayerWeights(weightsFlattened)
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

    #Pone los pesos finales en las matrices de cada layer
    def updateLayerWeights(self,finalW):
        #  currentIndex = 0
         for i in range(0,len(self.layers)):
            #Obtenemos las dimensiones de la layer en cuestion y el ultimo indice hasta el cual se deben agarrar los pesos
            rows,cols = self.layers[i].W.shape
            elemsCount = rows*cols 
            #Agarramos los pesos correspondientes
            currentWeights = finalW[:elemsCount]
            #Actualizamos los pesos, almacenandolos como una matriz con las dimensiones que correspondan
            self.layers[i].W = currentWeights.reshape(rows,cols)
            #Actualizamos el finalW para la proxima iteracion
            finalW = finalW[elemsCount:]
        