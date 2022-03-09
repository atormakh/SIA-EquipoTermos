class State:
    def __init__(self,towers,isGoal):
        self.towers=[]
        for tower in towers:
            self.towers.append(tower.copy())
        self.isGoal = isGoal