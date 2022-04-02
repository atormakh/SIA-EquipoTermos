class TimeFinishCondition:

    def __init__(self,maxExecutionTime):
        self.maxExecutionTime = maxExecutionTime

    def initializePopulationManager(self,populationManager):
        self.populationManager = populationManager

    def testCondition(self):
        return self.populationManager.currentExecutionTime >= self.maxExecutionTime

    @classmethod
    def fromJson(cls, finishConditionData):
        return cls(finishConditionData['max_execution_time'])

    @staticmethod
    def isValid(finishConditionData):
        isValid = True
        errorMessage = ""
        maxExecutionTime = None
        if('max_execution_time' in finishConditionData):
            maxExecutionTime = finishConditionData['max_execution_time']
        if(maxExecutionTime is None or not (isinstance(maxExecutionTime,int) or isinstance(maxExecutionTime,float)) or maxExecutionTime <= 0):
            isValid = False
            errorMessage = "Invalid Time Finish Condition. 'max_execution_time' is a required parameter and it must be a positive number"
        return (isValid,errorMessage)