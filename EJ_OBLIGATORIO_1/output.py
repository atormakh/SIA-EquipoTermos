
import os
from io import StringIO


class Output:
    def __init__(self,configParams, individuals,bestIndividual,executionTime,function):
        self.configParams = configParams
        self.bestIndividual= bestIndividual
        self.individuals = individuals
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

    # def writeToFile(self):
    #     csvRow = StringIO()
    #     try:
    #         currentMethodsCsvPath = f"./results/stats/{self.configParams.selectionData['method'].lower()}Selection_{self.configParams.crossData['method'].lower()}Cross_{self.configParams.mutationData['method'].lower()}Mutation_{self.configParams.finishConditionData['method'].lower()}FinishCondition.csv"
    #         globalCsvPath =  f"./results/stats/global.csv"

    #         #En caso de que no existan los csv correspondientes, se crean y se escriben los headers en cada uno
    #         if(not os.path.exists(currentMethodsCsvPath)):
    #             f = open(currentMethodsCsvPath,"a+")
    #             f.write("Selection,Cross,Mutation,Finish condition,generation,W1,W2,W3,w11,w12,w13,w21,w22,w23,w01,w02,F_1,F_2,F_3,Error,Fitness,Execution time (sec)\n")

    #         if(not os.path.exists(globalCsvPath)):
    #             f = open(globalCsvPath,"a+")
    #             f.write("Selection,Cross,Mutation,Finish condition,generation,W1,W2,W3,w11,w12,w13,w21,w22,w23,w01,w02,F_1,F_2,F_3,Error,Fitness,Execution time (sec)\n")
            
    #         #Escribir los metodos de seleccion, cruza, mutacion y criterio de corte utilizados, junto a la generacion del individuo optimo
    #         csvRow.write(f"{self.configParams.selectionData['method'].lower()},{self.configParams.crossData['method'].lower()},{self.configParams.mutationData['method'].lower()},{self.configParams.finishConditionData['method'].lower()},{len(self.populations)},")
    #         #Escribir los genes del individuo optimo
    #         for i in range(0,len(self.bestIndividual.genes)):
    #             csvRow.write(f"{self.bestIndividual.genes[i]},")
    #         #Escribir los valores de F(i)
    #         for i in range(0,len(self.optimalIndividualFValues)):
    #             csvRow.write(f"{self.optimalIndividualFValues[i]},")
    #         #Escribir el error, el fitness del individuo optimo y el tiempo de ejecucion
    #         csvRow.write(f"{self.fitness.error(self.bestIndividual)},{self.bestIndividual.fitness},{self.executionTime}\n")

    #         #Agregamos la linea escrita al csv correspondiente y al global
    #         f = open(currentMethodsCsvPath,"a+")
    #         f.write(csvRow.getvalue())
    #         f = open(globalCsvPath,"a+")
    #         f.write(csvRow.getvalue())

    #     # Do something with the file
    #     except IOError:
    #         print("File not accessible")
    # # Do something with the file