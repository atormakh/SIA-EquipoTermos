import random
import numpy as np

class Layer:
    def __init__(self, amountOfNodes,inputs,activationFunction):
        self.amountOfNodes=amountOfNodes
        self.inputs=inputs
        self.activationFunction=activationFunction
        #create weights matrix
        aux = self.__createWeightsMatrix()
        self.W = np.matrix(aux)

    def propagate(self,inputs):
        #multiply inputs with weights
        print('W :'+str(self.W),"--shape=",np.shape(self.W))
        print('inputs :'+str(inputs),"--shape=",np.shape(inputs))
        self.h = np.matmul(self.W,inputs).transpose()
        print("h=",str(self.h),"--shape==",np.shape(self.h))
        self.V = self.activationFunction.apply(self.h)
        return self.V

    def retroPropagate(self,upperLayerDelta,upperLayer):
        print("h==",self.h,"--shape==",np.shape(self.h))
        print("upperLayerW==",upperLayer.W,"--shape==",np.shape(upperLayer.W))
        print("upperLayerDelta==",upperLayerDelta,"--shape==",np.shape(upperLayerDelta))
       # print("upperMatrix==",np.matmul(upperLayer.W,upperLayerDelta),"--shape==",np.shape(np.matmul(upperLayer.W,upperLayerDelta)))
        self.delta = np.matmul(np.matmul(upperLayerDelta,upperLayer.W),self.activationFunction.applyDerivative(self.h))
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
                newCol.append(random.random())
            aux.append(newCol)
        return aux
        
#inputs = num columnas
#amountOfNodes= num filas
