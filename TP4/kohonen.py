
from cgi import test
from tkinter import N
import numpy as np

class Kohonen:
    def __init__(self, inputSize , n , radiusFunction= lambda t : np.sqrt(2) , learningFunction= lambda t : 1/t):
        self.n = n
        self.radiusFunction = radiusFunction
        self.learningFunction = learningFunction
        self.grid = self.__initializeGridRandom()
        self.inputSize = inputSize
        self.t = 1


    #Initialize functions
    
    def __getInitialWeight(self):
        return np.random.uniform(-1,1)

    def __initializeGridRandom(self):
        matrix = [] 
        for j in range(0 , self.n):
            row = []
            for i in range(0 , self.n):
                row.append( [self.__getInitialWeight() for k in range(0 , self.inputSize) ])
            matrix.append(row)    
        return np.array(matrix)

    
    #Exposed functions
    def train(self , xp):
        wk = test(xp)
        nearNeurons = self.__nearNeurons(wk)
        for n in nearNeurons:
            self.grid[n[0]][n[1]] = self.grid[n[0]][n[1]] + self.learningFunction(self.t) * (xp - self.grid[n[0]][n[1]])

        self.t += 1
        return wk


    def test(self , xp):
        minDistance = self.n ** 2
        position = ( -1 , -1 )
        for i in range(0 , self.n):
            for j in enumerate(0 , self.n):
                d = self.__wDistance(xp , self.grid[i][j])
                if d < minDistance:
                    minDistance = d
                    position = ( i , j )

        return position
    
    #
    def __isNear(self , p1 , p2):
        distance = np.sqrt((p1[0]-p2[0])**2 + (p1[0]-p2[0])**2 )
        return distance <= self.radiusFunction(self.t)

    def __nearNeurons(self , pos):
        near =  []
        for i in range(0 , self.n):
            for j in enumerate(0 , self.n):
                if self.__isNear(pos , (i , j)) and pos != (i,j):
                    near.append((i,j))
        return near

    def __wDistance(self , x1 , x2):
        aux = np.sum(np.square(x1 - x2))
        return np.sqrt(aux)




    