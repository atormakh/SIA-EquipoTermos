
import os
from io import StringIO


class Output:
    def __init__(self,configParams, bestIndividual,executionTime,function):
        self.configParams = configParams
        self.bestIndividual= bestIndividual
        self.executionTime=executionTime
        self.function = function
        self.optimalIndividualFValues = self.__getOptimalIndividualFValues()

    def __getOptimalIndividualFValues(self):
        optimalIndividualFValues = []
        for i in range(0,len(self.function.epsilon)):
            optimalIndividualFValues.append(self.function.f(self.bestIndividual.genes,self.function.epsilon[i]))
        return optimalIndividualFValues
    
    def __str__(self):
        return f"""OUTPUT :
        - Configuration paramaters :
            {self.configParams}
        - Solution :
            - Optimal individual: \n\t\t\t{self.bestIndividual.strArrays()}\n
                - F(i): {self.optimalIndividualFValues}\n
                - E(i): {self.function.error(self.bestIndividual.genes)}\n
        - Execution time : {self.executionTime} sec"""

    def __repr__(self) -> str:
        return self.__str__()

    def printOutput(self):
        print(self)
