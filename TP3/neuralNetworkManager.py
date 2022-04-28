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
        error = 2 * len(trainingSet) * len(resultsSet[0])
        while(np.absolute(error-0)<= np.power(10,self.maxToleranceExponent) or i <self.max_iterations ):
            #Reordenamos el trainingSet aleatoriamente para sacar conjuntos al azar
            trainingSet = np.random.shuffle(trainingSet)        
            for trainingArray in trainingSet: #[[1,1],[-1,1],[-1,-1],[1,-1]]
                # inputs=np.matrix(trainingSet[i]).transpose() #inputs = [1,-1]
                inputs = np.array(trainingArray).transpose()
                #propagate
                for layer in self.layers:
                    output= layer.propagate(inputs) #outputs=V=[-0.09,0.332]
                    inputs=output
                #backpropagation
                #Calculamos primero el delta de la capa correspondiente a la salida
                outputLayer = self.layers[-1]
                currentDelta = np.multiply(self.activationFunction.applyDerivative(outputLayer.h),np.substract(resultsSet,outputLayer.V))
                outputLayer.setDelta(currentDelta)
                #Realizamos la retropropagacion
                for i in range(len(self.layers)-2,-1,-1):
                    currentLayer = self.layers[i]
                    delta = currentLayer.retroPropagate(currentDelta,self.layers[i+1])
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
            error = self.__calculateError(resultsSet,outputArray)
            i+=1

            
                
    def __calculateError(self,resultsSet,outputSet):
        return 0.5 * sum(np.power(np.substract(resultsSet,outputSet),2))       
                
