from heuristicFunctions.secondHeuristicFunction import SecondHeuristicFunction
from searchAlgorithms.bfs import Bfs
from searchAlgorithms.dfs import Dfs
from searchAlgorithms.localHeuristic import LocalHeuristic
from searchAlgorithms.globalHeuristic import GlobalHeuristic
from heuristicFunctions.firstHeuristicFunction import FirstHeuristicFunction

class SearchHelper:

    def getSearchMethod(self,usedSearchMethod,initialState,game):
        if(usedSearchMethod == 'BPA'):
            return Bfs(initialState,game)
        elif(usedSearchMethod == 'BPP'):
            return Dfs(initialState,game)
        elif(usedSearchMethod == 'HL'):
            return LocalHeuristic(initialState,game)
        else:
            return GlobalHeuristic(initialState,game)

    def getHeuristicFunction(self,heuristicFunction,numberOfDisks,destinationTower):
        if(heuristicFunction == 'FHF'):
            return FirstHeuristicFunction(numberOfDisks,destinationTower)
        elif(heuristicFunction == 'SHF'):
            return SecondHeuristicFunction(numberOfDisks,destinationTower)