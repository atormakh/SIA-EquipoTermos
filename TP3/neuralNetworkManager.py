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

    def test(self,testingSet,resultsSet):
        
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
                for layer in self.layers:
                    output= layer.propagate(inputs)
                    inputs=output
                outputArray.append(inputs)

            error = self.__calculateError(resultsSet,outputArray)
        except Exception as e:
            error = errorDefault
            exception = True
        #Parar el cronometro
        endTime = time.perf_counter()            
        
        return (error,endTime-initTime,exception)
            
                
    def __calculateError(self,resultsSet,outputSet):
        #print("Result Set =",str(resultsSet), "outputSet", str(outputSet))
        error=0
        pow = lambda x: x**2
        for i in range(0,len(resultsSet)):
            diff=resultsSet[i]-outputSet[i]
            error+=0.5*np.sum(np.vectorize(pow)(diff))
        return  error/len(resultsSet)
        # return  error

    def crossValidation(self,trainingSet,resultsSet,k=None):
        
        error = None
        trainingPercentage = None
        maxKValue = len(trainingSet)

        #Primero, validamos el k
        if(k is None):
            k = maxKValue
        elif(not isinstance(k,int) or k<2 or k>maxKValue):
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
            # print('Training ',i+1)
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

            # print("current training set == ",currentTrainingSet)
            # print("current results set == ",currentResultsSet)


            #Entrenamos la red con el conjunto de entrenamiento y su salida
            # print('\tStart net training. . .')
            (trainingEpochs,trainingExecutionTime,trainingException) = self.start(currentTrainingSet,currentResultsSet)
            # print('\tNet training finished. . .')

            #Luego, lo probamos con el conjunto de testeo
            # print('\tStart net testing. . .')
            (testingError,testingExecutionTime,testingException) = self.test(testingSet,testingResultsSet)
            # print('\tNet testing finished. . .')

            #Checkeamos si el error de testeo es menor que el error minimo
            if(error is None or testingError<error):
                error = testingError

            #Si tiro excepcion en el testing, imprimimos y retornamos
            if(testingException):
                print(f"Cross validation with k={k} results:")
                print('\terror min ==',error)
                print('\ttraining percentage ==',trainingPercentage)

                return (error,trainingPercentage)

        
        print(f"Cross validation with k={k} results:")
        print('\terror min ==',error)
        print('\ttraining percentage ==',trainingPercentage)

        return (error,trainingPercentage)




class epoch:
    def __init__(self,iterationNumber,layers,error):
        self.iterationNumber=iterationNumber
        self.layers=layers
        self.error=error

                
