class  EliteSelection:
    def __init__(self):
        print("Hola TOR")

    def apply(self,selectionIndividuals,targetPopulationSize,replacement=False):
        #Ordenamos la poblacion por mayor fitness, y retornamos los primeros "targetPopulationSize"
        return sorted(selectionIndividuals,key=lambda x: x.fitness,reverse=True)[0:targetPopulationSize]

    @classmethod
    def fromJson(cls,selectionData):
        return cls()

    @staticmethod
    def isValid(selectionData,populationSize=None):
        return (True,"")

