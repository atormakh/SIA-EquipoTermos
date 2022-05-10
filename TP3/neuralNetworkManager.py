import math
import time
import copy
import numpy as np
from layer import Layer
class NeuralNetworkManager:
    def __init__(self,architecture,activationFunction,learningRate,maxEpochs,maxToleranceExponent):
        self.architecture=architecture
        self.activationFunction=activationFunction
        self.learningRate=learningRate
        self.maxEpochs=maxEpochs
        self.maxToleranceExponent = maxToleranceExponent
        #crear layers segun lo indique la arquitectura
        self.layers=[]
        for i in range(0,len(architecture)-1):
            self.layers.append(Layer(architecture[i+1],architecture[i],activationFunction))



    
    
    def start(self,trainingSet,resultsSet):
        
        #Iniciar el cronometro para medir el tiempo de ejecucion del algoritmo
        initTime = time.perf_counter()

        epochs=[]
        i=0
        exception=False
        error=None
        while((not exception) and (error==None or error>=math.pow(10,self.maxToleranceExponent)) and  i <self.maxEpochs ):
            try:
                #Reordenamos el trainingSet aleatoriamente para sacar conjuntos al azar, y reordenamos la salida de la misma manera
                combinatedTrainingResultSet = list(zip(trainingSet,resultsSet))
                np.random.shuffle(combinatedTrainingResultSet)
                shuffledTrainingSet, shuffledResultSet = zip(*combinatedTrainingResultSet)
                for tr in range(0,len(shuffledTrainingSet)): #[[1,1],[-1,1],[-1,-1],[1,-1]]
                    trainingArray=shuffledTrainingSet[tr]
                    inputs = np.matrix(trainingArray).transpose()
                    #propagate
                    for layer in self.layers:
                        
                        output= layer.propagate(inputs) 
                        inputs=output
                    #backpropagation
                    #Calculamos primero el delta de la capa correspondiente a la salida
                    outputLayer = self.layers[-1]
                    currentDelta = np.multiply(self.activationFunction.applyDerivative(outputLayer.h),np.subtract(np.matrix(shuffledResultSet[tr]).transpose(),outputLayer.V))
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

    def test(self,testingSet,resultsSet,metrics=None,layers=None):
        
        metricsDict = None
        #Iniciar el cronometro para medir el tiempo de ejecucion del algoritmo
        initTime = time.perf_counter()
        exception=False
        #Seteamos el error default
        errorDefault = 2 * len(resultsSet)
        #Realizar la propagacion
        try:
            outputArray = []
            for testingArray in testingSet:
                inputs = np.matrix(testingArray).transpose()
                #propagate
                if(layers is None):
                    layers=self.layers
                for layer in layers:
                    output= layer.propagate(inputs)
                    inputs=output
                outputArray.append(inputs)

            error = self.__calculateError(resultsSet,outputArray)
            if(math.isnan(error)):
                error = errorDefault
                exception = True
            #Si se paso la instancia de metricas, se calculan las metricas de la epoca
            if(metrics is not None):
                #Modificamos la matriz de confusion y obtenemos las metricas correspondientes
                metrics.modifyConfussionMatrix(resultsSet,outputArray)
                metricsDict = metrics.getMetrics()
        except Exception as e:
            print(e)
            error = errorDefault
            exception = True
        #Parar el cronometro
        endTime = time.perf_counter()            
        
        return (error,endTime-initTime,exception,metricsDict)
            
                
    def __calculateError(self,resultsSet,outputSet):
        #print("Result Set =",str(resultsSet), "outputSet", str(outputSet))
        error=0
        pow = lambda x: x**2
        for i in range(0,len(resultsSet)):
            diff=resultsSet[i]-outputSet[i]
            error+=0.5*np.sum(np.vectorize(pow)(diff))
        return  error/len(resultsSet)
        # return  error

    def crossValidation(self,trainingSet,resultsSet,k,metrics=None):
        
        error = None
        maxAccuracy = None
        trainingPercentage = None
        maxKValue = len(trainingSet)

        #Primero, validamos el k
        if(not isinstance(k,int) or k<2 or k>maxKValue):
            print(f"Illegal k : Should be an integer number between 2 and {maxKValue}")
            return (error,trainingPercentage)

        #Luego, calculamos el porcentaje del trainingSet utilizado para el entrenamiento
        trainingPercentage = 1 - 1/k

        #Luego, hacemos un shuffle en conjunto del trainingSet y el resultsSet
        combinatedTrainingResultSet = list(zip(trainingSet,resultsSet))
        np.random.shuffle(combinatedTrainingResultSet)
        # print(combinatedTrainingResultSet)

        #Luego, separamos el conjunto de trainingSet y resultsSet en k partes para obtener los distintos testingSet a utilizar en cada entrenamiento, junto con su salida esperada
        testingResultsSets = np.array_split(combinatedTrainingResultSet,k)

        #Realizamos los distintos entrenamientos (uno por cada testingSet a utilizar)
        for i in range(0,len(testingResultsSets)):
            testingSet, testingResultsSet = zip(*testingResultsSets[i])
            testingSet = list(testingSet)
            testingResultsSet = list(testingResultsSet)

            #Creamos el trainingSet a utilizar, y su salida correspondiente
            originalTrainingSet = copy.deepcopy(trainingSet)
            originalResultsSet = copy.deepcopy(resultsSet)

            for testingElem in testingSet:
                originalTrainingSet.remove(testingElem)
            
            for resultElem in testingResultsSet:
                originalResultsSet.remove(resultElem)

            currentTrainingSet = originalTrainingSet
            currentResultsSet = originalResultsSet

            #Si se paso la instancia de metricas, creamos una instancia de la misma para el testeo
            testingMetrics = None
            if(metrics is not None):
                testingMetrics = copy.deepcopy(metrics)

            #Entrenamos la red con el conjunto de entrenamiento y su salida
            (trainingEpochs,trainingExecutionTime,trainingException) = self.start(currentTrainingSet,currentResultsSet)

            #Luego, lo probamos con el conjunto de testeo
            (testingError,testingExecutionTime,testingException,testingMetricsDict) = self.test(testingSet,testingResultsSet,testingMetrics)

            #Checkeamos si el error de testeo es menor que el error minimo
            if(error is None or testingError<error):
                error = testingError

            #Nos guardamos la accuracy maxima en caso de que se haya pedido analizar las metricas
            if(metrics is not None and (maxAccuracy is None or testingMetricsDict['accuracy']>maxAccuracy)):
                maxAccuracy = testingMetricsDict['accuracy']

            #Si tiro excepcion en el testing, imprimimos y retornamos
            if(testingException):
                print(f"Cross validation with k={k} results:")
                print('\terror min ==',error)
                print('\ttraining percentage ==',trainingPercentage)
                if(metrics is not None):
                    print('\tmax accuracy == ',maxAccuracy)

                return (error,trainingPercentage,maxAccuracy)

        
        print(f"Cross validation with k={k} results:")
        print('\terror min ==',error)
        print('\ttraining percentage ==',trainingPercentage)
        if(metrics is not None):
            print('\tmax accuracy == ',maxAccuracy)

        return (error,trainingPercentage,maxAccuracy)




class epoch:
    def __init__(self,epochNumber,layers,error):
        self.epochNumber=epochNumber
        self.layers=layers
        self.error=error

                
