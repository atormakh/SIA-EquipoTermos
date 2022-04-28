from curses import ALL_MOUSE_EVENTS
from random import random
import numpy as np


class Layer:
    def __init__(self, amountOfNodes,inputs,activationFunction):
        self.amountOfNodes=amountOfNodes
        self.inputs=inputs
        self.activationFunction=activationFunction
        #create weights matrix
        self.W = np.matrix(self.__createWeightsMatrix())

    def propagate(self,inputs):
        #multiply inputs with weights
        self.h = np.multiply(self.W,inputs)
        self.V = self.activationFunction.apply(self.h)
        return self.V

    def retroPropagate(self,upperLayerDelta,upperLayer):
        self.delta = np.multiply(self.activationFunction.applyDerivative(self.h),np.multiply(upperLayer.W,upperLayerDelta))
        return self.delta

    def setDelta(self,delta):
        self.delta = delta

    def updateWeights(self,learningRate):
        for row in range(0,self.amountOfNodes):
            for column in range(0,self.inputs):
                deltaW = learningRate*self.delta[row]*self.inputs[column]
                self.W[row][column]+=deltaW

    def __createWeightsMatrix(self):
        aux = []
        for row in range(0,self.amountOfNodes):
            newCol=[]
            for column in range(0,self.inputs):
                newCol.append(np.random())
            aux.append(newCol)
        return aux
        
#inputs = num columnas
#amountOfNodes= num filas
