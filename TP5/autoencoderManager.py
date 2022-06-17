from layer import Layer
import time
import math
import numpy as np
from autograd.misc.optimizers import adam
from scipy.optimize import minimize
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
        self.currentStep = 1
        self.errors = []
        self.steps = []
        # wFinal = adam(nd.Gradient(self.errorHelper.error),self.getWeightsFlattened(),step_size=0.80085,num_iters=self.maxEpochs,callback=self.callbackFunctionAdam)
        wFinal = minimize(self.errorHelper.error,self.getWeightsFlattened(),args=(0),method='Powell',callback=self.callbackFunctionAdam, options={'maxiter': self.maxEpochs}).x 

        # #Actualizar los pesos de la red
        # self.updateLayerWeights(wFinal)
        
        # return (epochs,executionTime,exception)
    
        return (wFinal,self.errors[-1])


    #Devuelve los pesos de los layers como un array 1D
    def getWeightsFlattened(self):
        weightsFlattened = np.array([])
        for i in range(0,len(self.layers)):
            arr = (np.asarray(self.layers[i].W).flatten())
            weightsFlattened = np.concatenate([weightsFlattened,np.array(arr)],axis=0)
        
        return np.array(weightsFlattened)

    def callbackFunctionAdam(self,w):
        print('W : '+str(w))
        self.steps.append(self.currentStep)
        self.errors.append(self.errorHelper.error(w))
        self.currentStep+=1
