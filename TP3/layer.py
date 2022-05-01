import random
import numpy as np

HIDDEN_NODE_INPUT=1
class Layer:
    def __init__(self, amountOfNodes,numberOfInputs,activationFunction):
        self.amountOfNodes=amountOfNodes
        self.numberOfInputs=numberOfInputs
        self.activationFunction=activationFunction
        #create weights matrix
        aux = self.__createWeightsMatrix()
        self.W = np.matrix(aux)

    def propagate(self,inputs):
        inputs= np.insert(inputs,0,[HIDDEN_NODE_INPUT],axis=0)
        self.currentInput = inputs.transpose()
        #multiply inputs with weights
        #print('W :'+str(self.W),"--shape=",np.shape(self.W))
        #print('inputs :'+str(inputs),"--shape=",np.shape(inputs))
        self.h = np.matmul(self.W,inputs)
        # print("h=",str(self.h),"--shape==",np.shape(self.h))
        self.V = self.activationFunction.apply(self.h)
        # print("V=",str(self.V),"--shape==",np.shape(self.V))
        return self.V

    def retroPropagate(self,upperLayerDelta,upperLayer):
        activationFunctionDerivative = self.activationFunction.applyDerivative(self.h)
        activationFunctionDerivative= np.insert(activationFunctionDerivative,0,[HIDDEN_NODE_INPUT],axis=0)
        delta = np.multiply(activationFunctionDerivative,np.matmul(upperLayer.W.transpose(),upperLayerDelta))
        self.delta=  np.delete(delta,0,axis=0)
        return self.delta

    #########################################################################################################################################

    #     print("h==",self.h,"--shape==",np.shape(self.h))
    #     print("upperLayerW==",upperLayer.W,"--shape==",np.shape(upperLayer.W))
    #     print("upperLayerDelta==",upperLayerDelta,"--shape==",np.shape(upperLayerDelta))
    #    # print("upperMatrix==",np.matmul(upperLayer.W,upperLayerDelta),"--shape==",np.shape(np.matmul(upperLayer.W,upperLayerDelta)))
    #     print("delta*upperLayer==",np.matmul(upperLayerDelta,upperLayer.W),"--shape==",np.shape(np.matmul(upperLayerDelta,upperLayer.W)))
    #     print("g'(h)==",self.activationFunction.applyDerivative(self.h))
    #     print("g'(h)==",self.activationFunction.applyDerivative(self.h),"--shape==",np.shape(self.activationFunction.applyDerivative(self.h)))
    #     self.delta = np.matmul(np.matmul(upperLayerDelta,upperLayer.W),self.activationFunction.applyDerivative(self.h))
    #     return self.delta

    def setDelta(self,delta):
        self.delta = delta

    def updateWeights(self,learningRate):
        # print("delta==",self.delta,"--shape==",np.shape(self.delta))
        # print("input==",self.currentInput,"--shape",np.shape(self.currentInput))
        # print(self.inputs)
        #self.currentInput = self.currentInput.reshape([1,self.inputs])
        # print(" new input==",self.currentInput,"--shape",np.shape(self.currentInput))
        deltaAux=np.matmul(self.delta,self.currentInput)
        deltaW = np.multiply(learningRate,np.matmul(self.delta,self.currentInput))
        #deltaW = np.matrix(deltaW)
        self.W += deltaW

    def __createWeightsMatrix(self):
        aux = []
        for row in range(0,self.amountOfNodes):
            newCol=[]
            for column in range(0,self.numberOfInputs+1):
                newCol.append(random.random())
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
