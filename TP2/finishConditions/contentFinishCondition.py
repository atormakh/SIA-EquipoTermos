import math

class ContentFinishCondition:

    def __init__(self,maxGenerationSize,maxToleranceExponent):
        self.maxGenerationSize = maxGenerationSize
        self.maxToleranceExponent = maxToleranceExponent
        self.generationsWithSameMaxFitnessCount = 0

    def initializePopulationManager(self,populationManager):
        self.populationManager = populationManager

    def testCondition(self):
        #Chequea si se mantuvo o no el fitness maximo entre generaciones para ver como modificar el contador asociado
        self.__checkCurrentPopulationMaxFitness()
        #Una vez hecho eso, en caso de que el contador haya superado el valor maximo de generaciones, corta
        return self.generationsWithSameMaxFitnessCount >= self.maxGenerationSize

    def __checkCurrentPopulationMaxFitness(self):
        #Si hay mas de una poblacion en el historial, y el maximo fitness se mantiene igual ( utilizando la tolerancia indicada o la default) , se incrementa en 1 el contador correspondiente. Sino, vuelve a 0
        if(not len(self.populationManager.populationsHistory)== 1):
            currentPopulationMaxFitness = self.populationManager.populationsHistory[-1].maxFitnessIndividual.fitness
            lastPopulationMaxFitness = self.populationManager.populationsHistory[-2].maxFitnessIndividual.fitness
            #Si se paso la tolerancia como parametro, utiliza esa misma. Caso contrario utiliza la default (1e-9)
            maxFitnessRemainsEqual = math.isclose(currentPopulationMaxFitness,lastPopulationMaxFitness)
            if(self.maxToleranceExponent is not None):
                maxFitnessRemainsEqual = math.isclose(currentPopulationMaxFitness,lastPopulationMaxFitness,rel_tol=math.pow(10,self.maxToleranceExponent))
            if(maxFitnessRemainsEqual):
                self.generationsWithSameMaxFitnessCount+=1
            else:
                self.generationsWithSameMaxFitnessCount = 0

    @classmethod
    def fromJson(cls, finishConditionData):
        maxToleranceExponent = None
        if('max_tolerance_exponent' in finishConditionData):
            maxToleranceExponent = finishConditionData['max_tolerance_exponent']
        return cls(finishConditionData['max_generation_size'],maxToleranceExponent)

    @staticmethod
    def isValid(finishConditionData):
        isValid = True
        errorMessage = ""
        maxGenerationSize = None
        if('max_generation_size' in finishConditionData):
            maxGenerationSize = finishConditionData['max_generation_size']
        if(maxGenerationSize is None or not isinstance(maxGenerationSize,int) or maxGenerationSize <= 0):
            isValid = False
            errorMessage = "Invalid Content Finish Condition. 'max_generation_size' is a required parameter and it must be a positive integer number"
        maxToleranceExponent = None
        if('max_tolerance_exponent' in finishConditionData):
            maxToleranceExponent = finishConditionData['max_tolerance_exponent']
        if(maxToleranceExponent is not None and (not isinstance(maxToleranceExponent,int) or maxToleranceExponent>=0)):
            isValid = False
            errorMessage = "Invalid Content Finish Condition. 'max_tolerance_exponent' must be a negative integer number (less than zero)"
        return (isValid,errorMessage)