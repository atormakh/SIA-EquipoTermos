class Output:
    def __init__(self,algorithm,executionTime,resultSteps):
        self.algorithm=algorithm
        self.executionTime=executionTime
        self.resultSteps=resultSteps
    
    def __str__(self):
        return f"Solution for {self.algorithm}: \n----------------\n{str(self.resultSteps)}\n----------------\nTime:{str(self.executionTime)}\nSteps:{str(len(self.resultSteps))}"

    def __repr__(self) -> str:
        return self.__str__()