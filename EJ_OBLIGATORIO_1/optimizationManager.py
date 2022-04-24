import time
import numpy as np 
from individual import Individual

class OptimizationManager:

    def __init__(self,optimizationMethod,maxRangeGen,function):
        self.optimizationMethod = optimizationMethod
        self.maxRangeGen = maxRangeGen
        self.function = function


    def start(self):

        #Iniciar el cronometro para medir el tiempo de ejecucion del algoritmo
        initTime = time.perf_counter()

        #Setear el maximo rango de genes de los individuos
        Individual.setupIndividualsMaxRangeGen(self.maxRangeGen)

        #Generar individuo inicial
        initialIndividual=Individual()
        
        #Calcular optimo
        bestIndividualGenes = self.optimizationMethod.calculateOptimal(initialIndividual,self.function)
        bestIndividual = Individual(bestIndividualGenes)

        #Parar el cronometro
        endTime = time.perf_counter()

        return (bestIndividual,self.function.error(bestIndividual.genes),endTime-initTime)

    