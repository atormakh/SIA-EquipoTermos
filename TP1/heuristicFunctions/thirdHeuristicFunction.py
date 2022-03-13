class ThirdHeuristicFunction:

    def __init__(self,numberOfDisks,destinationTower):
        self.numberOfDisks = numberOfDisks
        self.destinationTower = destinationTower

    def calculateHeuristic(self,towers):
        ##Heuristica 3 : x + 2 * y
        #x : Cant de discos que no estan en la destination tower
        #y : Cant de discos en la destination tower para los cuales existe un disco mas grande en las otras towers

        #Primero, hallamos el indice correspondiente a la destination tower

        destinationTowerIndex = self.destinationTower -1

        #Luego, recorremos las otras torres para hallar la cantidad de discos en ellas

        otherTowersDiskCount = 0
        for i in range(len(towers)):
            if(i!=destinationTowerIndex):
                otherTowersDiskCount+=len(towers[i])
        
        #Luego, por cada disco de la destination tower, nos fijamos para cuantos de ellos existe un disco mas grande en las otras towers
        
        disksInDestTowerWithBiggerDisksInOtherTowersCount = 0
        destinationTower = towers[destinationTowerIndex]
        for i in range(len(destinationTower)):
            for j in range(len(towers)):
                if(j!=destinationTowerIndex):
                    otherTower = towers[j]
                    otherTowerIndex = 0
                    biggerDiskFound = False
                    while(not biggerDiskFound and otherTowerIndex!=len(otherTower)):
                        if(otherTower[otherTowerIndex]>destinationTower[i]):
                            biggerDiskFound = True
                            disksInDestTowerWithBiggerDisksInOtherTowersCount+=1
                        else:
                            otherTowerIndex+=1
        
        #Finalmente, retornamos la heuristica

        return otherTowersDiskCount + 2 * disksInDestTowerWithBiggerDisksInOtherTowersCount

