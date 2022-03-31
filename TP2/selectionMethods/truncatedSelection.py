import random
class TruncatedSelection:
    def __init__(self,k):
        if(k is None):
            print("Truncated Selection is missing K parameter")
        self.k=k

    def apply(self,selectionIndividuals,targetPopulationSize):
        selectedIndividuals = sorted(selectionIndividuals,key=lambda x: x.fitness,reverse=True)[:-self.k]
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