class SecondHeuristicFunction:
    
    def __init__(self,numberOfDisks,destinationTower):
        self.numberOfDisks = numberOfDisks
        self.destinationTower = destinationTower

    def calculateHeuristic(self,towers):
        ##Heuristica 2 : z + (x - y ) siendo
        #x : Cant de discos ---> self.numberOfDisks
        #y : Discos bien posicionados
        #z : Discos mal posicionados

        #Primero, creamos la torre ideal, con los discos ordenados
        idealDestinationTower = []
        for i in range(self.numberOfDisks):
            idealDestinationTower.append(self.numberOfDisks-i)
        
        #Luego, agarramos la torre correspondiente a la destination tower
        destinationTowerIndex = self.destinationTower-1
        destinationTower = towers[destinationTowerIndex]

        #Creamos variable para representar z e y previamente mencionados
        disksWellPositionedCount = 0
        disksBadPositionedCount = 0

        #Comparamos disco a disco
        i = 0
        while(disksBadPositionedCount==0 and i!=len(destinationTower)):
            if(destinationTower[i]==idealDestinationTower[i]):
                disksWellPositionedCount+=1
                i+=1
            else:
                #Si un disco esta mal, todos los siguientes tambien
                disksBadPositionedCount=len(destinationTower)-i
        
        #Finalmente, retornamos la heuristica
        return disksBadPositionedCount + (self.numberOfDisks - disksWellPositionedCount)


