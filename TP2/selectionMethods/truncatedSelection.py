import random
class TruncatedSelection:
    def __init__(self,k):
        if(k is None):
            print("Truncated Selection is missing K parameter")
        self.k=k

    def apply(self,selectionIndividuals,targetPopulationSize,replacement=False):
        selectedIndividuals = sorted(selectionIndividuals,key=lambda x: x.fitness,reverse=True)[:-self.k]
        #Si k = P, ya me quedaron los P individuos seleccionados
        if(self.k == targetPopulationSize):
            return selectedIndividuals
        #Sino, los selecciono de distinta forma dependiendo si es con o sin reemplazo
        if(not replacement):
            return random.sample(selectedIndividuals,targetPopulationSize)
        outputIndividuals=[]
        for i in range(0,targetPopulationSize):
            outputIndividuals.append(selectedIndividuals[random.randint(0,len(selectedIndividuals)-1)])
        return outputIndividuals

    @classmethod
    def fromJson(cls,selectionData):
        return cls(selectionData['k'])

    @staticmethod
    def isValid(selectionData):
        isValid = True
        errorMessage = ""
        k = None
        if('k' in selectionData):
         k=selectionData['k']
        if(k is None or  not isinstance(k,int)):
            isValid = False
            errorMessage="Invalid Truncated Selection parameters. 'k' is a required parameter and it must be an integer lower than 2 times the population size"          
        return (isValid,errorMessage)