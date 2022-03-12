class FirstHeuristicFunction:
    
    def __init__(self,numberOfDisks,destinationTower):
        self.numberOfDisks = numberOfDisks
        self.destinationTower = destinationTower

    def calculateHeuristic(self,towers):
        ##Heuristica 1 : Cant de discos totales - cant de discos posicionados correctamente en la destination tower
        destinationTowerIndex = self.destinationTower -1
        destinationTower = towers[destinationTowerIndex]
        if(len(destinationTower)==0 or len(destinationTower)==1):
            return self.numberOfDisks - len(destinationTower)
        disksWellPositionedCount = 0
        i = 0
        while(i != len(destinationTower)-1 and (destinationTower[i]==destinationTower[i+1]+1)):
            disksWellPositionedCount += 1
            i += 1
        if(i == len(destinationTower)-1):
            disksWellPositionedCount += 1
        return self.numberOfDisks - disksWellPositionedCount
