from mimetypes import init
from searchAlgorithms.f import F
from searchAlgorithms.bfs import Bfs
from searchAlgorithms.dfs import Dfs
from searchAlgorithms.vdfs import Vdfs
from searchAlgorithms.vdfsOptimo import VdfsOptimo
from searchAlgorithms.localHeuristicRecursive import LocalHeuristic
from heuristicFunctions.firstHeuristicFunction import FirstHeuristicFunction
from heuristicFunctions.secondHeuristicFunction import SecondHeuristicFunction
from heuristicFunctions.thirdHeuristicFunction import ThirdHeuristicFunction

class SearchHelper:

    def getSearchMethod(self,usedSearchMethod,initialState,game,maxHeightBppv=None , growthFactorBppv = None):
        if(usedSearchMethod == 'BPA'):
            return Bfs(initialState,game)
        elif(usedSearchMethod == 'BPP'):
            return Dfs(initialState,game)
        elif(usedSearchMethod == 'BPPV'):
            return Vdfs(initialState,game,maxHeightBppv , growthFactorBppv)
        elif(usedSearchMethod == 'BPPVO'):
            return VdfsOptimo(initialState,game,maxHeightBppv , growthFactorBppv)
        elif(usedSearchMethod == 'HL'):
            return LocalHeuristic(initialState,game)
        elif(usedSearchMethod == 'HG'):
            return F(initialState,game,0,1)
        elif(usedSearchMethod == 'A*'):
            return F(initialState,game,0.5,0.5)
        else:
            return None

    def getHeuristicFunction(self,heuristicFunction,numberOfDisks,destinationTower):
        if(heuristicFunction is None):
            return None
        if(heuristicFunction == 'FHF'):
            return FirstHeuristicFunction(numberOfDisks,destinationTower)
        elif(heuristicFunction == 'SHF'):
            return SecondHeuristicFunction(numberOfDisks,destinationTower)
        else:
            return ThirdHeuristicFunction(numberOfDisks,destinationTower)