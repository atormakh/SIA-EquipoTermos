import random
import numpy as np
from numba import jit

#W0s
HIDDEN_NODE_INPUT=1
class Layer:
    def __init__(self, amountOfNodes,numberOfInputs,activationFunction):
        self.amountOfNodes=amountOfNodes
        self.numberOfInputs=numberOfInputs
        self.activationFunction=activationFunction
        #create weights matrix
        aux = self.__createWeightsMatrix()
        #self.W = np.matrix(aux)
        self.W = np.array(aux)
        self.lastDelta = None

    def propagate(self,inputs):
        # inputs= np.insert(inputs,0,[HIDDEN_NODE_INPUT],axis=0)
        self.currentInput = inputs.transpose()
        self.h = np.matmul(self.W,inputs)
        self.V = self.activationFunction.apply(self.h)
        return self.V
        
    @jit(nopython=True)
    def propagateMatrix(self,inputs):
      #  print(f'inputMatrix = {len(inputs)} x {len(inputs[0])}')
        self.currentInputMatrix = inputs
      #  print(f'W = {len(self.W)} x {len(self.W[0])}')
        return self.activationFunction.apply(np.matmul(self.W , self.currentInputMatrix))
      

    def retroPropagate(self,upperLayerDelta,upperLayer):
        activationFunctionDerivative = self.activationFunction.applyDerivative(self.h)
        activationFunctionDerivative= np.insert(activationFunctionDerivative,0,[HIDDEN_NODE_INPUT],axis=0)
        delta = np.multiply(activationFunctionDerivative,np.matmul(upperLayer.W.transpose(),upperLayerDelta))
        self.delta=  np.delete(delta,0,axis=0)
        return self.delta

    def setDelta(self,delta):
        self.delta = delta

    def updateWeights(self,learningRate , momentum=0):
        deltaW = np.multiply(learningRate,np.matmul(self.delta,self.currentInput))
        self.W += deltaW
        deltaMomentum = 0 
        if self.lastDelta is not None:
            deltaMomentum = np.dot(momentum , deltaW)
            self.W += deltaMomentum
        self.lastDelta = deltaW + deltaMomentum

    def __createWeightsMatrix(self):
        aux = []
        for row in range(0,self.amountOfNodes):
            newCol=[]
            for column in range(0,self.numberOfInputs):
                newCol.append(np.random.uniform(-1,1))
            aux.append(newCol)
        return aux

    def __str__(self):
        return f"""
        - W: {self.W}
        - h: {self.h}
        - V: {self.V}
        - delta: {self.delta}"""

    def __repr__(self) -> str:
        return self.__str__()

        
#inputs = num columnas
#amountOfNodes= num filas
