from population import Population

class PopulationManager:

    def __init__(self,maxGenerationSize,populationSize,crossMethod,selectionMethod,mutation,fitness,crossIndexCount=None):
        self.maxGenerationSize = maxGenerationSize
        self.populationSize = populationSize
        self.crossMethod = crossMethod
        self.crossIndexCount = crossIndexCount
        self.selectionMethod = selectionMethod
        self.mutation = mutation
        self.fitness = fitness
        self.populationsHistory = []
        self.currentGeneration = 0


    def start(self):
        #Generar poblacion inicial
        initialPopulation = Population(self.currentGeneration,self.fitness)
        initialPopulation.createInitialIndividuals(self.populationSize)

        currentPopulation=initialPopulation

        #Agrego la generacion 0 al historial
        self.populationsHistory.append(currentPopulation)
        #Mientras no cumpla criterio de corte
        while( self.currentGeneration<self.maxGenerationSize):
                
            #Crear nueva poblacion
            newIndividuals=[]

            #Mientras la poblacion nueva no tenga cantidad populationSize
            while( len(newIndividuals) < self.populationSize ):
                
                #Elijo random 2 individuos de la poblacion vieja
                
                randomIndividuals = currentPopulation.getRandomIndividuals(2)

                #Cruzo a dichos individuos para obtener 2 descendientes

                [newIndividual1,newIndividual2] = self.crossMethod(randomIndividuals[0],randomIndividuals[1],self.crossIndexCount)
                
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

            newIndividuals = self.selectionMethod(selectionIndividuals,self.populationSize)
            newPopulation = Population(self.currentGeneration+1,self.fitness,newIndividuals)
            #Reemplazo la poblacion vieja por la nueva

            currentPopulation = newPopulation

            #Agrego la nueva poblacion al historial
            self.populationsHistory.append(currentPopulation)

            print('Current population : '+str(currentPopulation))


            #Aumento en 1 el numero de generacion
            self.currentGeneration+=1

        return (currentPopulation.maxFitnessIndividual,self.populationsHistory)