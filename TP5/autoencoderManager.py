from layer import Layer
import time
import math
import numpy as np
from autograd.misc.optimizers import adam
from scipy.optimize import minimize
import numdifftools as nd
from helpers.errorHelper import ErrorHelper

class AutoencoderManager:
    
    def __init__(self,architecture,encoderActivationFunction,latentSpaceActivationFunction,decoderActivationFunction,learningRate,maxEpochs):
        self.architecture=architecture
        # self.activationFunction=activationFunction
        self.encoderActivationFunction = encoderActivationFunction
        self.latentSpaceActivationFunction = latentSpaceActivationFunction
        self.decoderActivationFucntion = decoderActivationFunction
        self.learningRate=learningRate
        self.maxEpochs=maxEpochs
    
        #crear layers segun lo indique la arquitectura
        self.layers=[]
        for i in range(0,len(architecture)-1):
            self.layers.append(Layer(architecture[i+1],architecture[i],self.__getActivationFunction(i)))

    def initilizeWeights(self,trainingSet,initialWeight):
        self.errorHelper = ErrorHelper(trainingSet,self.layers)
        self.errorHelper.updateLayerWeights(initialWeight)


    def start(self,trainingSet):
        
        #Iniciar el cronometro para medir el tiempo de ejecucion del algoritmo
        self.initTime = time.perf_counter()

        self.errorHelper = ErrorHelper(trainingSet,self.layers)
        self.currentStep = 1
        self.errors = []
        self.steps = []
        self.stepStartTime = time.perf_counter()
        # wFinal = adam(nd.Gradient(self.errorHelper.error),self.getWeightsFlattened(),step_size=0.80085,num_iters=self.maxEpochs,callback=self.callbackFunctionAdam)
        wFinal = minimize(self.errorHelper.error,self.getWeightsFlattened(),args=(0),method='Powell',callback=self.callbackFunctionAdam, options={'maxiter': self.maxEpochs}).x 

        # #Actualizar los pesos de la red
        # self.updateLayerWeights(wFinal)
        
        # return (epochs,executionTime,exception)
        self.wFinal = wFinal
        return (wFinal,self.errors[-1])
    
    def propagate(self,trainingCharacter):

        return self.errorHelper.propagateCharacter(trainingCharacter)

    def getLatentSpaceConfig(self,characterArray):
        return self.errorHelper.getLatentSpaceConfig(characterArray)


    #Devuelve los pesos de los layers como un array 1D
    def getWeightsFlattened(self):
        weightsFlattened = np.array([])
        for i in range(0,len(self.layers)):
            arr = (np.asarray(self.layers[i].W).flatten())
            weightsFlattened = np.concatenate([weightsFlattened,np.array(arr)],axis=0)
        
        return np.array(weightsFlattened)

    def callbackFunctionAdam(self,w):
        # print('W : '+str(w))
        endStepTime = time.perf_counter()
        print('Iteration : ',self.currentStep)
        error = self.errorHelper.error(w)
        print('\tError : ',error)
        print('\tTime : ',endStepTime-self.stepStartTime)
        self.stepStartTime = endStepTime
        self.steps.append(self.currentStep)
        self.errors.append(error)
        self.currentStep+=1

    def __getActivationFunction(self,layerIndex):
        latentSpaceIndex = len(self.architecture)//2-1
        if(layerIndex<latentSpaceIndex):
            return self.encoderActivationFunction
        elif(layerIndex>latentSpaceIndex):
            return self.decoderActivationFucntion
        else:
            return self.latentSpaceActivationFunction
