class State:


    def __init__(self,towers,isGoal):
        tupledTowers = []
        for tower in towers:
            tupledTowers.append(tuple(tower))
        self.towers = tuple(tupledTowers) 
        self.isGoal = isGoal
    
    def __str__(self):
        return f'{{Towers: {str(self.towers)}, isGoal: {str(self.isGoal)} }}'
#, {[f"towerLen {i}: {len(tower)}" for i, tower in enumerate(self.towers)]}
    def __repr__(self):
        return self.__str__()
    # def sortedEq(self , v1  , v2):
    #     if( len(v1) != len(v2)):
    #         return False
    #     for i in range(len(v1)):
    #         if(v1[i] != v2[i]):
    #             return False
    # return True 
    
    def __eq__(self,other):
        return self.towers == other.towers
        
    # if( len(self.towers) != len(other.towers)):
    #    return False
    # Al parecer el == intenta sortearlo, tendriamos que hacer un sorted eq
    # return all( (self.towers[i] == other.towers[i]) for i in range(len(self.towers)) ) 
    #
    
    def mutableState(self):
        mutable = []
        for tower in self.towers:
            mutable.append(list(tower))
        return mutable

    def __hash__(self):
        return hash(self.towers)