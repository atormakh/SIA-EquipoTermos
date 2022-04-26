import numpy as np
from layer import Layer

class NeuralNetworkManager:
    def __init__(self,architecture,activationFunction,learningRate,max_iterations):
        self.architecture=architecture
        self.activationFunction=activationFunction
        self.learningRate=learningRate
        self.max_iterations=max_iterations
        #crear layers segun lo indique la arquitectura
        self.layers=[]
        
        for i in range(0,len(architecture)-1): #[3,1] len([3,1])=2 2-1=1 range(0,1)
            self.layers.append(Layer(architecture[i+1],architecture[i],activationFunction))



    
    
    def start(self,trainingSet,resultsSet):
        i=0
        while(i <self.max_iterations ):        
            for i in trainingSet:
                inputs=np.matrix(trainingSet[i]).transpose() #inputs = [1,-1]
                #propagate
                for layer in self.layers:
                    output= layer.propagate(inputs) #outputs=V=[-0.09,0.332]
                    inputs=output
                #backpropagation
                
                    #change weights
                
