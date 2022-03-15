class Output:
    def __init__(self,configParams,searchSucceded,solutionCost,solutionHeight,expandedNodesCount,frontierNodesCount,resultSteps,executionTime):
        self.configParams = configParams
        if(searchSucceded):
            self.searchResult = 'Success'
            self.solution = resultSteps
            self.solutionCost = solutionCost
            self.solutionHeight = solutionHeight
        else:
            self.searchResult = 'Fail'
            self.solution = 'No solution available'
            self.solutionCost = 0
            self.solutionHeight = 0
        
        self.expandedNodesCount = expandedNodesCount
        self.frontierNodesCount = frontierNodesCount
        self.executionTime=executionTime

    # def __init__(self,algorithm,executionTime,resultSteps):
    #     self.algorithm=algorithm
    #     self.executionTime=executionTime
    #     self.resultSteps=resultSteps
    
    def __str__(self):
        # return f"Solution for {self.algorithm}: \n----------------\n{str(self.resultSteps)}\n----------------\nTime:{str(self.executionTime)}\nSteps:{str(len(self.resultSteps))}"
        return f"OUTPUT : \n--------\n -Configuration paramaters :\n  {str(self.configParams)}\n -Search result : {self.searchResult}\n -Solution : {self.solution}\n -Solution cost : {self.solutionCost}\n -Solution height : {self.solutionHeight}\n -Expanded nodes count : {self.expandedNodesCount}\n -Frontier nodes count : {self.frontierNodesCount}\n -Execution time : {self.executionTime} sec"

    def __repr__(self) -> str:
        return self.__str__()

    def printOutput(self):
        print(self)

    def writeToFile(self):
        try:
            if(self.configParams.searchMethod == 'A*'):
                self.configParams.searchMethod = "Aestrella"
            f = open(f"./results/stats/{self.configParams.searchMethod}.csv" , "a+")
            f.write(f"{self.configParams.searchMethod},{self.configParams.diskCount},{self.executionTime},{self.solutionHeight},{self.expandedNodesCount},{self.frontierNodesCount},{self.configParams.heuristicFunction}\n")
            fg = open(f"./results/stats/global.csv", "a+")
            fg.write(f"{self.configParams.searchMethod},{self.configParams.diskCount},{self.executionTime},{self.solutionHeight},{self.expandedNodesCount},{self.frontierNodesCount},{self.configParams.heuristicFunction}\n")
        # Do something with the file
        except IOError:
            print("File not accessible")
    # Do something with the file