import random
class TournamentSelection:
    def __init__(self,u):
        if(u is None):
            print("Tournament Selection is missing u parameter")
        self.u=u
        self.tournamentSize = 4
        self.tournamentIndividuals = []
        #Primero, inicializar el array de los individuos del torneo
        self.__initializeTournamentIndividuals()

    def apply(self,selectionIndividuals,targetPopulationSize,replacement=False):
        outputSelection=[]

        for i in range(0,targetPopulationSize):
            #elegir aleatoriamente dos parejas de individuos de la poblacion
            self.__setSelectionIndividuals(selectionIndividuals)

            winners=[self.tournamentIndividualsCompetition(self.tournamentIndividuals[0],self.tournamentIndividuals[1]),self.tournamentIndividualsCompetition(self.tournamentIndividuals[2],self.tournamentIndividuals[3])]
            winnerIndividual = self.tournamentIndividualsCompetition(winners[0],winners[1])
            outputSelection.append(winnerIndividual)
            #Si no es con reemplazo, saco al individuo ganador
            if(not replacement):
                 selectionIndividuals.remove(winnerIndividual)
                 #Reiniciar el array de individuos para la siguiente iteracion
                 self.__resetTournamentIndividuals()
        return outputSelection
        
    def tournamentIndividualsCompetition(self,i1=None,i2=None):
        winner=None
        #En caso de que los 2 individuos sean None, el ganador es None
        if(i1 is None and i2 is None):
            return winner
        #En caso de que uno de los 2 sea None, el ganador es el otro
        if(i1 is not None and i2 is None):
            return i1
        if(i1 is None and i2 is not None):
            return i2
        #En caso de que ninguno sea None, compiten para ver quien gana
        r = random.uniform(0,1)
        if r<self.u:
            winner= i1 if i1.fitness >= i2.fitness else i2
        else:
            winner = i2 if i1.fitness >= i2.fitness else i1
        return winner

    def __initializeTournamentIndividuals(self):
        for i in range(0,self.tournamentSize):
            self.tournamentIndividuals.append(None)

    def __resetTournamentIndividuals(self):
        for i in range(0,self.tournamentSize):
            self.tournamentIndividuals[i]=None

    def __setSelectionIndividuals(self,selectionIndividuals):
        selectionsIndividualsLength = len(selectionIndividuals)
        #Si 2P < 4, hacer competencia entre todos los individuos. Sino, compiten solo 4
        if(selectionsIndividualsLength < self.tournamentSize):
            tournamentIndividuals = random.sample(selectionIndividuals,selectionsIndividualsLength)
            for i in range(0,selectionsIndividualsLength):
                self.tournamentIndividuals[i] = tournamentIndividuals[i]
        else:
            self.tournamentIndividuals = random.sample(selectionIndividuals,self.tournamentSize)


    @classmethod
    def fromJson(cls,selectionData):
        return cls(selectionData['u'])

    @staticmethod
    def isValid(selectionData,populationSize=None):
        isValid = True
        errorMessage = ""
        u=selectionData['u']
        if(u is None or  not isinstance(u,float) or u < 0.5 or u > 1):
            isValid = False
            errorMessage="Invalid Tournament Selection parameters. 'u' is a required parameter and it must be a float betweet 0.5 and 1."          
        return (isValid,errorMessage)