import math

class AcceptableSolutionFinishCondition:

    def __init__(self,maxToleranceExponent):
        self.maxToleranceExponent = maxToleranceExponent
    
    def initializePopulationManager(self,populationManager):
        self.populationManager = populationManager

    def testCondition(self):
        #Agarrar el individuo con mejor fitness de la ultima poblacion y el error del mismo
        lastPopulationMaxIndividualFitness = self.populationManager.populationsHistory[-1].maxFitnessIndividual
        error = self.populationManager.fitness.error(lastPopulationMaxIndividualFitness)

        #Luego, la condicion de corte se cumple si el error es cercano a 0, o si el fitness es cercano al maximo, utilizando la tolerancia de error indicada
        return math.fabs(error-0)<= math.pow(10,self.maxToleranceExponent) or math.isclose(lastPopulationMaxIndividualFitness.fitness,self.populationManager.fitness.maxFitness,rel_tol = math.pow(10,self.maxToleranceExponent))
        

    @classmethod
    def fromJson(cls, finishConditionData):
        return cls(finishConditionData['max_tolerance_exponent'])

    @staticmethod
    def isValid(finishConditionData):
        isValid = True
        errorMessage = ""
        maxToleranceExponent = None
        if('max_tolerance_exponent' in finishConditionData):
            maxToleranceExponent = finishConditionData['max_tolerance_exponent']
        if(maxToleranceExponent is None or not isinstance(maxToleranceExponent,int) or maxToleranceExponent>=0):
            isValid = False
            errorMessage = "Invalid Acceptable Solution Finish Condition. 'max_tolerance_exponent' is a required parameter and must be a negative integer number (less than zero)"
        return (isValid,errorMessage)