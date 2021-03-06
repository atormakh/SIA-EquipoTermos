import time
from individual import Individual
from population import Population

class PopulationManager:

    def __init__(self,populationSize,maxRangeGen,replacement,crossMethod,selectionMethod,mutation,fitness,finishCondition):
        self.populationSize = populationSize
        self.maxRangeGen = maxRangeGen
        self.replacement = replacement
        self.crossMethod = crossMethod
        self.selectionMethod = selectionMethod
        self.mutation = mutation
        self.fitness = fitness
        self.populationsHistory = []
        self.finishCondition = finishCondition
        self.currentGeneration = 0
        self.currentExecutionTime = 0


    def start(self):

        #Iniciar el cronometro para medir el tiempo de ejecucion del algoritmo
        initTime = time.perf_counter()

        #Setear el maximo rango de genes de los individuos
        Individual.setupIndividualsMaxRangeGen(self.maxRangeGen)

        #Inicializar el population manager en la condicion de corte
        self.finishCondition.initializePopulationManager(self)

        #Generar poblacion inicial
        initialPopulation = Population(self.currentGeneration,self.fitness)
        initialPopulation.createInitialIndividuals(self.populationSize)

        currentPopulation=initialPopulation

        #Agregar la generacion 0 al historial
        self.populationsHistory.append(currentPopulation)

        #Tomar el tiempo de ejecucion actual
        self.currentExecutionTime = time.perf_counter() - initTime

        #Mientras no cumpla criterio de corte
        while( not self.finishCondition.testCondition()):
                
            #Crear nueva poblacion
            newIndividuals=[]

            #Mientras la poblacion nueva no tenga cantidad populationSize
            while( len(newIndividuals) < self.populationSize ):
                
                #Elijo random 2 individuos de la poblacion vieja
                randomIndividuals = currentPopulation.getRandomIndividuals(2,self.replacement)

                #Cruzo a dichos individuos para obtener 2 descendientes
                [newIndividual1,newIndividual2] = self.crossMethod.apply(randomIndividuals[0],randomIndividuals[1])
                
                #Aplico mutacion a los descendientes
                
                self.mutation.apply(newIndividual1)
                self.mutation.apply(newIndividual2)

                #Calcular el fitness de cada individuo
                newIndividual1.fitness = self.fitness.calculate(newIndividual1)
                newIndividual2.fitness = self.fitness.calculate(newIndividual2)

                #Agrego los descendientes a la poblacion nueva

                newIndividuals.append(newIndividual1)
                newIndividuals.append(newIndividual2)
                
            #Aplico metodo de seleccion a la poblacion total para quedarme con una de cantidad populationSize
            selectionIndividuals = []
            selectionIndividuals.extend(currentPopulation.individuals)
            selectionIndividuals.extend(newIndividuals)
            newIndividuals = self.selectionMethod.apply(selectionIndividuals,self.populationSize,self.replacement)
            newPopulation = Population(self.currentGeneration+1,self.fitness,newIndividuals)
            #Reemplazo la poblacion vieja por la nueva

            currentPopulation = newPopulation

            #Agrego la nueva poblacion al historial
            self.populationsHistory.append(currentPopulation)

            print('Current population : '+str(currentPopulation))


            #Aumento en 1 el numero de generacion
            self.currentGeneration+=1

            #Seteo el nuevo tiempo de ejecucion actual para la proxima iteracion
            self.currentExecutionTime = time.perf_counter() - initTime

         #Parar el cronometro
        endTime = time.perf_counter()

        return (currentPopulation.maxFitnessIndividual,self.populationsHistory,endTime-initTime)