import random
from individual import Individual

class Population:
    
    def __init__(self,generation,fitness,individuals=None):
        self.generation=generation
        if(individuals is None):
            self.individuals = []
        else:
            self.individuals = individuals
            self._calculateBestIndividual()
        self.fitness = fitness

    def createInitialIndividuals(self,numberOfIndividuals):
        maxFitnessIndividual=None
        for i in range(0,numberOfIndividuals):
            #Creo individuo con genes random y lo agrego a la coleccion
            individual = Individual()
            self.individuals.append(individual) 
            #Calculo su fitness
            individualFitness = self.fitness.calculate(individual)
            individual.fitness=individualFitness
            #Me fijo si es el individuo con mejor fitness
            if(maxFitnessIndividual is None):
                maxFitnessIndividual=individual
            else:
                if(maxFitnessIndividual.fitness <= individualFitness):
                    maxFitnessIndividual=individual

        #Me guardo el individuo con mayor fitness
        self.maxFitnessIndividual=maxFitnessIndividual

    def _calculateBestIndividual(self):
        self.maxFitnessIndividual = self.individuals[0]
        for individual in self.individuals:
            if(self.maxFitnessIndividual.fitness <= individual.fitness):
                self.maxFitnessIndividual=individual

    def getRandomIndividuals(self,numberOfIndividuals):
        randomIndividuals = []
        for i in range(0,numberOfIndividuals):
            randIndex = random.randint(0,len(self.individuals)-1)
            randomIndividuals.append(self.individuals[randIndex])
        return randomIndividuals

    def __str__(self):
        return f"Population:{{Generation: {self.generation}, MaxFitness:{self.maxFitnessIndividual.fitness}}}"

    def __repr__(self):
        return self.__str__()