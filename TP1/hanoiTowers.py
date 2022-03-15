from state import State


class HanoiTowers:
    def __init__(self,numberOfDisks,destinationTower,heuristicFunction):
        self.numberOfDisks=numberOfDisks
        self.destinationTower=destinationTower
        self.heuristicFunction=heuristicFunction

    def generateInitialState(self):
        firstTower = []

        for i in range(self.numberOfDisks):
            firstTower.append( self.numberOfDisks - i )

        return State([firstTower , [] , [] ], False)

    def peek(self,tower):
        length = len(tower)
        if(length == 0 ):
        #Setear a uno mas grande que le torre base
            return self.numberOfDisks + 1
        else:
            return tower[length-1]

    def areWinningTowers(self,towers):
        for i in range(len(towers)):
            if( i == (self.destinationTower-1) and len(towers[i]) == self.numberOfDisks):
                return True 

        return False

    def possibleMoves(self , state,heuristic=False):

        if(not self.validateState(state)):
            print("State is invalid")
            return []
            
        moves = []    
        towers = state.towers
        towerRange = range(len(towers))
        
        for i in towerRange:
            if(len(towers[i]) > 0 ): #Si tengo algo en la torre, significa que puedo comenzar un movimiento
                top = self.peek(towers[i]) #Top es la ficha a mover
                for j in towerRange:
                    if( i != j ): #Me fijo en las otras torres si puedo pasar mi ficha de arriba
                        if(top < self.peek(towers[j])):      
                            #Crear un nuevo estado donde esta poppeado y pasa a la otra torre
                            moves.append(self.createNewState(state.mutableState(), i , j,heuristic))
        return moves

    def createNewState(self,towers, startingTower , endingTower,heuristic=False):
        newTowers = []
        for tower in towers:
            newTowers.append(tower.copy())

        top = newTowers[startingTower].pop()
        newTowers[endingTower].append(top)
        return State(newTowers , self.areWinningTowers(newTowers),self.heuristicFunction.calculateHeuristic(newTowers) if heuristic else None)


    ##Se creo un metodo para validar que es un disco valido (int y entre 1 y el maximo)

    def validDisk(self,disk):
        return isinstance(disk,int) and disk>=1 and disk<=self.numberOfDisks 

    def validTower(self,tower):
        if(len(tower) == 0 or (len(tower) == 1 and self.validDisk(tower[0]))):
            return True

        return all((self.validDisk(tower[i]) and tower[i] > tower[i + 1]) for i in range(len(tower)-1))

 
    def validateState(self , state):
        
        ##Esto es para verificar que la cantidad de discos sea la especificada
        totalLengthTowers = 0
        for tower in state.towers:
            totalLengthTowers+=len(tower)
        return (totalLengthTowers==self.numberOfDisks) and all( self.validTower(state.towers[i]) for i in range(len(state.towers)))
