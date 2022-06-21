import imp
import math
from typing import final
import numpy as np

class ErrorHelper:

    def __init__(self,trainingSet,layers,resultsSet=None):
        self.trainingSet = trainingSet
        self.layers = layers
        self.trainingSetTransposed = [ np.array(x).transpose() for x in trainingSet]
        self.trainingMatrix = np.array(self.trainingSetTransposed).transpose()
        print(f'training matrix {self.trainingMatrix.shape}')
        self.resultsSet = trainingSet
        if(resultsSet is not None):
            self.resultsSet = resultsSet

    def error(self,weightsFlattened,step=None):
        outputArray = []
        #Actualizamos los pesos de las layers
        self.updateLayerWeights(weightsFlattened)
        outputArray = self.propagateMatrix(self.trainingMatrix)
        error=0
        for d in zip(self.resultsSet , outputArray):
            diff = d[0]-d[1]
            error+=np.sum(np.square(diff))
        error = error * 0.5
      
        return  error/len(self.trainingSet)

    def propagateCharacter(self,characterArray):
        inputs = characterArray
        #propagate
        for layer in self.layers:
            inputs=layer.propagate(inputs)
        return inputs

    def propagateMatrix(self,trainingSet):
        inputs = trainingSet
        for layer in self.layers:
            inputs=layer.propagateMatrix(inputs)
        return inputs.transpose()

    def getLatentSpaceConfig(self,characterArray):
        inputs = np.array(characterArray).transpose()
        for i in range(0, len(self.layers)//2):
            inputs=self.layers[i].propagate(inputs)
        return inputs

    def decodeFromLatentSpace(self,latentSpace):
        #Decodificamos la matriz de latentSpace
        inputs = np.array(latentSpace).transpose()
        for i in range(len(self.layers)//2,len(self.layers)):
            inputs=self.layers[i].propagate(inputs)
        return inputs

    #Pone los pesos finales en las matrices de cada layer
    def updateLayerWeights(self,finalW):
        for layer in self.layers:
            rows,cols = layer.W.shape
            elemsCount = rows*cols

            currentsWeights = finalW[:elemsCount]

            layer.W = currentsWeights.reshape(rows,cols)

            finalW = finalW[elemsCount:]