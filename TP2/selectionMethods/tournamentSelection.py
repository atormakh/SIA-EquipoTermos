import random


class TournamentSelection:
    def __init__(self,u):
        if(u is None):
            print("Tournament Selection is missing u parameter")
        self.u=u

    def apply(self,selectionIndividuals,targetPopulationSize):
        outputSelection=[]
        for i in range(0,targetPopulationSize):
            #elegir aleatoriamente dos parejas de individuos de la poblacion
            tournamentIndividuals = []
            for i in range(0,4):
                tournamentIndividuals.append(selectionIndividuals[random.randint(0,len(selectionIndividuals)-1)])

            winners=[self.tournamentIndividuals(tournamentIndividuals[0],tournamentIndividuals[1]),self.tournamentIndividuals(tournamentIndividuals[2],tournamentIndividuals[3])]
            outputSelection.append(self.tournamentIndividuals(winners[0],winners[1]))
        return outputSelection
        
    def tournamentIndividuals(self,i1,i2):
        winner=None
        r = random.uniform(0,1)
        if r<self.u:
            winner= i1 if i1.fitness >= i2.fitness else i2
        else:
            winner = i2 if i1.fitness >= i2.fitness else i1
        return winner

    @classmethod
    def fromJson(cls,selectionData):
        return cls(selectionData['u'])

    @staticmethod
    def isValid(selectionData):
        isValid = True
        errorMessage = ""
        u=selectionData['u']
        if(u is None or  not isinstance(u,float)):
            isValid = False
            errorMessage="Invalid Tournament Selection parameters. 'u' is a required parameter and it must be a float betweet 0.5 and 1."          
        return (isValid,errorMessage)