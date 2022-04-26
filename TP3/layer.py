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
        return self.activationFunction.apply(h)

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
