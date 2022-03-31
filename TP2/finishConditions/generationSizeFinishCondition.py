class GenerationSizeFinishCondition:

    def __init__(self,maxGenerationSize):
        self.maxGenerationSize = maxGenerationSize

    def initializePopulationManager(self,populationManager):
        self.populationManager = populationManager

    def testCondition(self):
        return self.populationManager.currentGeneration >= self.maxGenerationSize

    @classmethod
    def fromJson(cls, finishConditionData):
        return cls(finishConditionData['max_generation_size'])

    @staticmethod
    def isValid(finishConditionData):
        isValid = True
        errorMessage = ""
        maxGenerationSize = None
        if('max_generation_size' in finishConditionData):
            maxGenerationSize = finishConditionData['max_generation_size']
        if(maxGenerationSize is None or not isinstance(maxGenerationSize,int) or maxGenerationSize <= 0):
            isValid = False
            errorMessage = "Invalid Generation Size Finish Condition. 'max_generation_size' is a required parameter and it must be a positive integer number"
        return (isValid,errorMessage)