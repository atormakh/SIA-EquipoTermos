import math
import numpy as np

class Fitness:

    def __init__(self,epsilon,c):
        self.epsilon = epsilon
        self.c = c
        self.maxFitness = len(self.epsilon)
    
    # X = (W0, W1, W2, w11, w12, w13, w21, w22, w23, , w01, w02)

    def f(self,individual,epsilon):
        #Modelamos los genes del individuo como los arrays y matrices mostrados en el enunciado
        W = np.array(individual.genes[0:3])
        w = np.array([individual.genes[3:6],individual.genes[6:9]])
        w0 = np.array(individual.genes[9:11])

        (rowsCount, columsCount) = w.shape

        #Calculamos la funcion F
        
        totalAcum = 0

        for j in range(0,rowsCount):
            colAcum = 0
            for k in range(0,columsCount):
                colAcum+=(w[j][k]*epsilon[k])
            totalAcum += (W[j]*self.g(colAcum-w0[j]))
        return self.g(totalAcum - W[0])

    def g(self,x):
        try:
            return math.exp(x)/(1+math.exp(x))
        except:
            return 1

    def error(self,individual):
        error = 0
        for i in range(0,len(self.epsilon)):
         error +=  math.pow((self.c[i]- self.f(individual,self.epsilon[i])),2)
        return error

    def calculate(self,individual):
        return self.maxFitness - self.error(individual)
        