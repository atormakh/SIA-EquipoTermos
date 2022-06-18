import math
from typing import final
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
            propagation_output = self.propagateCharacter(trainingArray)
            outputArray.append(propagation_output)
            
        #print("Result Set =",str(resultsSet), "outputSet", str(outputSet))
        error=0
        for d in zip(self.resultsSet , outputArray):
            diff = d[0]-d[1]
            error+=np.sum(np.square(diff))
        error = error * 0.5
        return  error/len(self.resultsSet)

    def propagateCharacter(self,characterArray):
        inputs = np.array(characterArray).transpose()
        #propagate
        for layer in self.layers:
            inputs=layer.propagate(inputs)
        return inputs

    #Pone los pesos finales en las matrices de cada layer
    def updateLayerWeights(self,finalW):
        #  currentIndex = 0
        # for i in range(0,len(self.layers)):
        #     #Obtenemos las dimensiones de la layer en cuestion y el ultimo indice hasta el cual se deben agarrar los pesos
        #     rows,cols = self.layers[i].W.shape
        #     elemsCount = rows*cols 
        #     #Agarramos los pesos correspondientes
        #     currentWeights = finalW[:elemsCount]
        #     #Actualizamos los pesos, almacenandolos como una matriz con las dimensiones que correspondan
        #     self.layers[i].W = currentWeights.reshape(rows,cols)
        #     #Actualizamos el finalW para la proxima iteracion
        #     finalW = finalW[elemsCount:]
        
        for layer in self.layers:
            rows,cols = layer.W.shape
            elemsCount = rows*cols
            #Saco los primeros elementos de un array ??
            currentsWeights = finalW[:elemsCount]

            layer.W = currentsWeights.reshape(rows,cols)

            finalW = finalW[elemsCount:]