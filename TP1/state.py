class State:
    def __init__(self,towers,isGoal,heuristic=None):
        tupledTowers = []
        for tower in towers:
            tupledTowers.append(tuple(tower))
        self.towers = tuple(tupledTowers) 
        self.isGoal = isGoal
        self.heuristic=heuristic
        self.hash = hash(self.towers)
    
    def __str__(self):
        return f'{{Towers: {str(self.towers)}, isGoal: {str(self.isGoal)}{f", heuristic={self.heuristic}" if self.heuristic is not None else ""} }}'
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self,other):
        return self.towers == other.towers
    
    def mutableState(self):
        mutable = []
        for tower in self.towers:
            mutable.append(list(tower))
        return mutable

    def __hash__(self):
        return hash(self.towers)