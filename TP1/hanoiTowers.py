from state import State


class HanoiTowers:
    def __init__(self) -> None:
        pass

    def peek(self,tower):
        length = len(tower)
        if(length == 0 ):
        #Setear a uno mas grande que le torre base
            return 99999
        else:
            return tower[length-1]


    def possibleMoves(self , state):

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
                            moves.append(self.createNewState(towers, i , j))
                            
        return moves

    def createNewState(self,towers, startingTower , endingTower):
        newTowers = []
        
        for tower in towers:
            newTowers.append(tower.copy())

        top = newTowers[startingTower].pop()
        newTowers[endingTower].append(top)
        return State(newTowers , False)  

    def validTower(self,tower):
        if(len(tower) == 0 or len(tower) == 1):
            return True
        return all(tower[i] >= tower[i + 1] for i in range(len(tower)-1))

    def validateState(self , state):
        return all(self.validTower(state.towers[i]) for i in range(len(state.towers)-1))
