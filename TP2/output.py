class Output:
    def __init__(self,configParams, populations,bestIndividual,executionTime,fitness):
        self.configParams = configParams
        self.bestIndividual= bestIndividual
        self.populations=populations
        self.executionTime=executionTime
        self.fitness = fitness
        self.optimalIndividualFValues = self.__getOptimalIndividualFValues()

    def __getOptimalIndividualFValues(self):
        optimalIndividualFValues = []
        for i in range(0,len(self.fitness.epsilon)):
            optimalIndividualFValues.append(self.fitness.f(self.bestIndividual,self.fitness.epsilon[i]))
        return optimalIndividualFValues
    
    def __str__(self):
        return f"""OUTPUT :
        - Configuration paramaters :
            {self.configParams}
        - Solution :
            - Generation: {len(self.populations)}
            - Optimal individual: \n\t\t\t{self.bestIndividual.strArrays()}\n
            - F(i): {self.optimalIndividualFValues}\n
            - E(i): {self.fitness.error(self.bestIndividual)}\n
            - Fitness : {self.bestIndividual.fitness}\n
        - Execution time : {self.executionTime} sec"""

    def __repr__(self) -> str:
        return self.__str__()

    def printOutput(self):
        print(self)

    def writeToFile(self):
        try:
            f = open(f"./results/stats/{self.configParams.searchMethod}.csv" , "a+")
            f.write(f"{self.configParams.selectionData.get('method')},{self.configParams.populationSize},{len(self.populations)},{self.exectutionTime}\n")
            fg = open(f"./results/stats/global.csv", "a+")
            fg.write(f"{self.configParams.selectionData.get('method')},{self.configParams.populationSize},{len(self.populations)},{self.exectutionTime}\n")
        # Do something with the file
        except IOError:
            print("File not accessible")
    # Do something with the file