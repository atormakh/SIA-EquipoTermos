from layer import Layer
import time
import numpy as np
from autograd.misc.optimizers import adam
import numdifftools as nd
from helpers.errorHelper import ErrorHelper

class AutoencoderManager:
    
    def __init__(self,architecture,activationFunction,learningRate,maxEpochs):
        self.architecture=architecture
        self.activationFunction=activationFunction
        self.learningRate=learningRate
        self.maxEpochs=maxEpochs
    
        #crear layers segun lo indique la arquitectura
        self.layers=[]
        for i in range(0,len(architecture)-1):
            self.layers.append(Layer(architecture[i+1],architecture[i],activationFunction))

    def start(self,trainingSet,resultsSet):
        
        #Iniciar el cronometro para medir el tiempo de ejecucion del algoritmo
        initTime = time.perf_counter()

        self.errorHelper = ErrorHelper(trainingSet,resultsSet,self.layers)
        wFinal = adam(nd.Gradient(self.errorHelper.error),self.getWeightsFlattened(),step_size=0.80085,num_iters=self.maxEpochs)
        # return (epochs,executionTime,exception)
    
        return wFinal


    #Devuelve los pesos de los layers como un array 1D
    def getWeightsFlattened(self):
        weightsFlattened = np.array([])
        for i in range(0,len(self.layers)):
            arr = (np.asarray(self.layers[i].W).flatten())
            weightsFlattened = np.concatenate([weightsFlattened,np.array(arr)],axis=0)
        
        return np.array(weightsFlattened)