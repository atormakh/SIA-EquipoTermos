import time
import math
import random
import numpy as np 
from individual import Individual

class OptimizationManager:

    def __init__(self,optimizationMethod,maxRangeGen,maxToleranceExponent,function):
        self.optimizationMethod = optimizationMethod
        self.maxRangeGen = maxRangeGen
        self.maxToleranceExponent = maxToleranceExponent
        self.function = function
        self.individualsHistory = []
        self.currentEpoch = 0


    def start(self):

        #Iniciar el cronometro para medir el tiempo de ejecucion del algoritmo
        initTime = time.perf_counter()

        #Setear el maximo rango de genes de los individuos
        Individual.setupIndividualsMaxRangeGen(self.maxRangeGen)

        #Generar individuo inicial
        currentIndividual=Individual()

        #Agregar el individuo 0 al historial
        self.individualsHistory.append(currentIndividual)

        #Declarar el individuo optimo
        bestIndividual = currentIndividual

        print('individual 0 : '+str(currentIndividual))

        #Checkear si el metodo de optimizacion se hara mediante el proceso general de optimizacion o no
        if(self.optimizationMethod.useGeneralAlgorithm):

            print('Hecho con el algoritmo (a descomentar despues)')
            
            # #Mientras no el error no se acerque a 0 con la tolerancia especificada
            # while( math.fabs(self.function.error(currentIndividual)-0) > math.pow(10,self.maxToleranceExponent)):
                    
            #     #Calculamos alpha
            #     alpha = random.random()

            #     #Calculamos la direccion de descenso
            #     direction = (-1) * self.optimizationMethod.calculateDirection(currentIndividual)
            #     npDirArray = np.array(direction)
                
            #     #Calculamos el vector de alpha*d
            #     npAlphaDirArray = np.multiple(npDirArray,alpha)

            #     #Y luego, creamos al nuevo individuo
            #     npIndividualGenes = np.array(currentIndividual.genes)
            #     newIndividualGenes = np.add(npIndividualGenes,npAlphaDirArray)
            #     newIndividual = Individual(newIndividualGenes)
                
            #     #Agrego el nuevo individuo al historial
            #     self.individualsHistory.append(newIndividual)

            #     #Reemplazo el current individual
            #     currentIndividual = newIndividual

            #     print('Current individual : '+str(currentIndividual))

            #     #Aumento en 1 el numero de epoca
            #     self.currentEpoch+=1
        
        else:
            print('Hecho sin el algoritmo')
            bestIndividualGenes = self.optimizationMethod.calculateOptimal(currentIndividual,self.function)
            bestIndividual = Individual(bestIndividualGenes)

        #Parar el cronometro
        endTime = time.perf_counter()

        return (bestIndividual,self.individualsHistory,endTime-initTime)

    