import numpy as np

class Kohonen:
    def __init__(self, inputSize , k , r0, maxEpochs, initialLearningRate, trainingSet, namesSet, initialRandomWeights=False):
        self.inputSize = inputSize
        self.k = k
        self.r0 = r0
        self.maxEpochs = maxEpochs
        self.initialLearningRate = initialLearningRate
        self.trainingSet = trainingSet
        self.namesSet = namesSet
        self.radiusFunction = lambda t : self.__decayRadius(t)
        self.learningFunction = lambda t : self.__decayLearningRate(t)
        self.initialRandomWeights = initialRandomWeights
        self.grid = self.__initializeGridRandom()
        self.t = 1

    #Funciones de inicializacion
    
    def __getInitialWeight(self):
        return np.random.uniform(-1,1)

    def __initializeGridRandom(self):
        matrix = [] 
        for j in range(0 , self.k):
            row = []
            for i in range(0 , self.k):
                weights = []
                for k in range(0 , self.inputSize):
                    weight = np.random.choice(self.trainingSet[:,k],size=1)[0]
                    if(self.initialRandomWeights):
                        weight = self.__getInitialWeight()
                    weights.append(weight)
                row.append(weights)
            matrix.append(row)    
        return np.array(matrix)

    
    #Funciones expuestas
    def train(self,t):
        #Reordenamos el trainingSet aleatoriamente para sacar conjuntos al azar, y reordenamos el set de nombres (en nuestro caso los paises) de la misma manera
        combinatedTrainingNamesSet = list(zip(self.trainingSet,self.namesSet))
        np.random.shuffle(combinatedTrainingNamesSet)
        shuffledTrainingSet, shuffledNamesSet = zip(*combinatedTrainingNamesSet)
        #Creamos una matriz para mapear los distintos paises a las neuronas de salida
        countriesMatrix = np.empty((self.k,self.k),object)
        #Actualizamos el t
        self.t = t
        #Iteramos por el trainingSet
        for i in range(0,len(shuffledTrainingSet)):
            xp = shuffledTrainingSet[i]
        # self.t = t
            wk = self.test(xp)
            nearNeurons = self.__nearNeurons(wk)
            for n in nearNeurons:
                self.grid[n[0]][n[1]] = self.grid[n[0]][n[1]] + self.learningFunction(self.t) * (xp - self.grid[n[0]][n[1]])
            #Insertamos el pais en la matriz
            if(countriesMatrix[wk[0]][wk[1]] is None):
                countriesMatrix[wk[0]][wk[1]] = [shuffledNamesSet[i]]
            else:
                countriesMatrix[wk[0]][wk[1]].append(shuffledNamesSet[i])

        #Devolvemos la matriz de paises
        return countriesMatrix


    def test(self , xp):
        minDistance = self.k ** 2
        position = ( -1 , -1 )
        for i in range(0 , self.k):
            for j in range(0 , self.k):
                d = self.__wDistance(xp , self.grid[i][j])
                if d < minDistance:
                    minDistance = d
                    position = ( i , j )

        return position

    def createUMatrix(self):
        #Creamos la matriz U de kxk
        uMatrix = np.zeros((self.k,self.k))
        for i in range(0,self.k):
            for j in range(0,self.k):
                sumDistances = 0
                currentNeuron = ( i , j )
                #Buscamos las neuronas vecinas a la actual
                nearNeurons = self.__nearNeurons(currentNeuron)
                #Por cada neurona vecina, acumulamos las distancias euclideas entre el vector de pesos de la neurona actual y la neurona vecina correspondiente
                for nearNeuron in nearNeurons:
                    currentNeuronWeights = self.grid[currentNeuron[0]][currentNeuron[1]]
                    nearNeuronWeights = self.grid[nearNeuron[0]][nearNeuron[1]]
                    sumDistances = sumDistances + self.__wDistance(currentNeuronWeights,nearNeuronWeights)
                #Luego, en la posicion i,j de la matriz U insertamos el promedio de dichas distancias
                uMatrix[i][j] = sumDistances/len(nearNeurons)
        return uMatrix

    def createUMatrixPerCharacteristic(self,characteristicIndex):
        characteristicUMatrix = np.zeros((self.k,self.k))
        for i in range(0,self.k):
            for j in range(0,self.k):
                sumDistances = 0
                currentNeuron = ( i , j )
                #Buscamos las neuronas vecinas a la actual
                nearNeurons = self.__nearNeurons(currentNeuron)
                #Por cada neurona vecina, acumulamos las distancias euclideas entre el vector de pesos de la neurona actual y la neurona vecina correspondiente
                for nearNeuron in nearNeurons:
                    currentNeuronCharacteristic = self.grid[currentNeuron[0]][currentNeuron[1]][characteristicIndex]
                    nearNeuronCharacteristic = self.grid[nearNeuron[0]][nearNeuron[1]][characteristicIndex]
                    sumDistances = sumDistances + np.sqrt(np.square(currentNeuronCharacteristic-nearNeuronCharacteristic))
                #Luego, en la posicion i,j de la matriz U insertamos el promedio de dichas distancias
                characteristicUMatrix[i][j] = sumDistances/len(nearNeurons)
        return characteristicUMatrix
    
    #
    def __isNear(self , p1 , p2):
        distance = np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )
        return distance <= self.radiusFunction(self.t)

    def __nearNeurons(self , pos):
        near =  []
        for i in range(0 , self.k):
            for j in range(0 , self.k):
                if self.__isNear(pos , (i , j)) and pos != (i,j):
                    near.append((i,j))
        return near

    def __wDistance(self , x1 , x2):
        aux = np.sum(np.square(x1 - x2))
        return np.sqrt(aux)

    def __decayRadius(self,t):
        return self.r0 * np.exp(-t*(np.log(self.r0)/self.maxEpochs))

    def __decayLearningRate(self,t):
        return self.initialLearningRate * (1/t)

