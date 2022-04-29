import math
import numpy as np
from layer import Layer

class NeuralNetworkManager:
    def __init__(self,architecture,activationFunction,learningRate,max_iterations,maxToleranceExponent):
        self.architecture=architecture
        self.activationFunction=activationFunction
        self.learningRate=learningRate
        self.max_iterations=max_iterations
        self.maxToleranceExponent = maxToleranceExponent
        #crear layers segun lo indique la arquitectura
        self.layers=[]
        for i in range(0,len(architecture)-1): #[3,1] len([3,1])=2 2-1=1 range(0,1)
            self.layers.append(Layer(architecture[i+1],architecture[i],activationFunction))



    
    
    def start(self,trainingSet,resultsSet):
        i=0
        error = 2 * len(trainingSet) * len(resultsSet)#math.fabs(error)<= np.power(10,self.maxToleranceExpsonent) or
        while( i <self.max_iterations ):
            print('Iteration ',i,' starting. . .')
            #Reordenamos el trainingSet aleatoriamente para sacar conjuntos al azar
            np.random.shuffle(trainingSet)
            for tr in range(0,len(trainingSet)): #[[1,1],[-1,1],[-1,-1],[1,-1]]
                # inputs=np.matrix(trainingSet[i]).transpose() #inputs = [1,-1]
                trainingArray=trainingSet[tr]
                inputs = np.array(trainingArray).transpose()
                #propagate
                j=0
                for layer in self.layers:
                    output= layer.propagate(inputs) #outputs=V=[-0.09,0.332]
                    inputs=output
                    j+=1
                #backpropagation
                #Calculamos primero el delta de la capa correspondiente a la salida
                outputLayer = self.layers[-1]
                # print("output H==",outputLayer.h,"--shape==",np.shape(outputLayer.h))
                # print("resultSets=",resultsSet,"--shape==",np.shape(resultsSet[tr]))
                # print("outputLayer V",outputLayer.V,"--shape==",np.shape(outputLayer.V))
                currentDelta = np.multiply(self.activationFunction.applyDerivative(outputLayer.h),np.subtract(resultsSet[tr],outputLayer.V))
                # print("DELTA ==",currentDelta)
                outputLayer.setDelta(currentDelta)
                #Realizamos la retropropagacion
                for j in range(len(self.layers)-2,-1,-1):
                    currentLayer = self.layers[j]
                    delta = currentLayer.retroPropagate(currentDelta,self.layers[j+1])
                    currentDelta = delta    
                #change weights
                for layer in self.layers:
                    layer.updateWeights(self.learningRate)
            #Calculamos el error e incrementamos el numero de
            outputArray = []
            for trainingArray in trainingSet:
                inputs = np.array(trainingArray).transpose()
                #propagate
                for layer in self.layers:
                    output= layer.propagate(inputs)
                    inputs=output
                    outputArray.append(layer.V)
            # error = self.__calculateError(resultsSet,outputArray)
            print('Iteration ',i,' finishing. . .')
            i+=1
        #Imprimimos las layers
        print("FINAL LAYERS")
        for k in range(0,len(self.layers)):
            print(self.layers[k])
            
                
    def __calculateError(self,resultsSet,outputSet):
        return 0.5 * sum(np.power(np.subtract(resultsSet,outputSet),2))       
                
