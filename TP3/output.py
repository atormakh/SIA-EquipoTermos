
import os
from io import StringIO


class Output:
    def __init__(self,configParams, error, epoch, executionTime):
        self.configParams = configParams
        self.error = error
        self.epoch = epoch
        self.executionTime = executionTime 
    
    def __str__(self):
        return f"""OUTPUT :
        - Configuration paramaters :
            {self.configParams}
        - Error : {self.error}\n
        - Epoch : {self.epoch}\n
        - Execution time : {self.executionTime} sec"""

    def __repr__(self) -> str:
        return self.__str__()

    def printOutput(self):
        print(self)