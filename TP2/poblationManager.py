from poblation import Poblation

class PoblationManager:

    def __init__(self,maxGenerationSize,poblationSize,crossMethod,selectionMethod,fitness):
        self.maxGenerationSize = maxGenerationSize
        self.poblationSize = poblationSize
        self.crossMethod = crossMethod
        self.selectionMethod = selectionMethod
        #self.mutation = mutation
        self.fitness = fitness
        self.poblationsHistory = []
        self.currentGeneration = 0


    def start(self):
        #Generar poblacion inicial
        initialPoblation = Poblation(self.currentGeneration,self.fitness)
        initialPoblation.createInitialIndividuals(self.poblationSize)

        currentPoblation=initialPoblation

        #Agrego la generacion 0 al historial
        self.poblationsHistory.append(currentPoblation)
        print("FIRST GENERATION==")
        for individual  in currentPoblation.individuals:
            print(individual)
        #Mientras no cumpla criterio de corte
        while( self.currentGeneration<self.maxGenerationSize):
                
            #Crear nueva poblacion
            newIndividuals=[]

            #Mientras la poblacion nueva no tenga cantidad poblationSize
            while( len(newIndividuals) < self.poblationSize ):
                
                #Elijo random 2 individuos de la poblacion vieja
                
                randomIndividuals = currentPoblation.getRandomIndividuals(2)

                #Cruzo a dichos individuos para obtener 2 descendientes

                [newIndividual1,newIndividual2] = self.crossMethod(randomIndividuals[0],randomIndividuals[1])
                
                #Aplico mutacion a los descendientes
                
                #mutation.apply(newIndividual1)
                #mutation.apply(newIndividual2)

                #Calcular el fitness de cada individuo
                newIndividual1.fitness = self.fitness.calculate(newIndividual1)
                newIndividual2.fitness = self.fitness.calculate(newIndividual2)

                #Agrego los descendientes a la poblacion nueva

                newIndividuals.append(newIndividual1)
                newIndividuals.append(newIndividual2)
                
            #Aplico metodo de seleccion a la poblacion total para quedarme con una de cantidad poblationSize
            selectionIndividuals = []
            selectionIndividuals.extend(currentPoblation.individuals)
            selectionIndividuals.extend(newIndividuals)

            newIndividuals = self.selectionMethod(selectionIndividuals,self.poblationSize)
            newPoblation = Poblation(self.currentGeneration+1,self.fitness,newIndividuals)
            #Reemplazo la poblacion vieja por la nueva

            currentPoblation = newPoblation

            #Agrego la nueva poblacion al historial
            self.poblationsHistory.append(currentPoblation)

            print('Current poblation : '+str(currentPoblation))


            #Aumento en 1 el numero de generacion
            self.currentGeneration+=1

        return currentPoblation.maxFitnessIndividual