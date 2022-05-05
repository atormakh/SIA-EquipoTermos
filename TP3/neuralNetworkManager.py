import math
import time
import copy
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
        
        #Iniciar el cronometro para medir el tiempo de ejecucion del algoritmo
        initTime = time.perf_counter()

        epochs=[]
        i=0
        #error = 2 * len(trainingSet) * len(resultsSet)#math.fabs(error)<= np.power(10,self.maxToleranceExpsonent) or
        exception=False
        error=None
        while((not exception) and (error==None or error>=math.pow(10,self.maxToleranceExponent)) and  i <self.max_iterations ):
            try:
                #print('Iteration ',i,' starting. . .')
                #Reordenamos el trainingSet aleatoriamente para sacar conjuntos al azar, y reordenamos la salida de la misma manera
                combinatedTrainingResultSet = list(zip(trainingSet,resultsSet))
                np.random.shuffle(combinatedTrainingResultSet)
                shuffledTrainingSet, shuffledResultSet = zip(*combinatedTrainingResultSet)
                # np.random.shuffle(trainingSet)
                for tr in range(0,len(shuffledTrainingSet)): #[[1,1],[-1,1],[-1,-1],[1,-1]]
                    # inputs=np.matrix(trainingSet[i]).transpose() #inputs = [1,-1]
                    trainingArray=shuffledTrainingSet[tr]
                    inputs = np.matrix(trainingArray).transpose()
                    #propagate
                    for layer in self.layers:
                        
                        output= layer.propagate(inputs) #outputs=V=[-0.09,0.332]
                        inputs=output
                    #backpropagation
                    #Calculamos primero el delta de la capa correspondiente a la salida
                    outputLayer = self.layers[-1]
                    #print("output H==",outputLayer.h,"--shape==",np.shape(outputLayer.h))
                # print("resultSets=",resultsSet[tr],"--shape==",np.shape(resultsSet[tr]),"--shapeMatrix===",np.shape(np.matrix(resultsSet[tr]).transpose()))
                    #print("outputLayer V",outputLayer.V,"--shape==",np.shape(outputLayer.V))
                # substract = np.subtract(np.matrix(resultsSet[tr]).transpose(),outputLayer.V)
                    #print("substract==",substract,"--shape==",np.shape(substract))
                    currentDelta = np.multiply(self.activationFunction.applyDerivative(outputLayer.h),np.subtract(np.matrix(shuffledResultSet[tr]).transpose(),outputLayer.V))
                    #print("DELTA ==",currentDelta)
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
                    inputs = np.matrix(trainingArray).transpose()
                    #propagate
                    for layer in self.layers:
                        output= layer.propagate(inputs)
                        inputs=output
                    outputArray.append(inputs)
                # plotPointsEj1(self.layers[0].W,trainingSet,i)
                error = self.__calculateError(resultsSet,outputArray)
                epochs.append(epoch(i,copy.deepcopy(self.layers),error))
                i+=1
            except Exception as e:
                exception=True

        #Parar el cronometro
        endTime = time.perf_counter()            
        
        return (epochs,endTime-initTime,exception)
            
                
    def __calculateError(self,resultsSet,outputSet):
        #print("Result Set =",str(resultsSet), "outputSet", str(outputSet))
        error=0
        pow = lambda x: x**2
        for i in range(0,len(resultsSet)):
            diff=resultsSet[i]-outputSet[i]
            error+=0.5*np.sum(np.vectorize(pow)(diff))
        return  error/len(resultsSet)
        # return  error




class epoch:
    def __init__(self,iterationNumber,layers,error):
        self.iterationNumber=iterationNumber
        self.layers=layers
        self.error=error

                
