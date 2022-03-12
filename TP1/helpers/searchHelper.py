from searchAlgorithms.localHeuristic import LocalHeuristic
from searchAlgorithms.bfs import Bfs
from searchAlgorithms.dfs import Dfs

class SearchHelper:

    def getSearchMethod(self,usedSearchMethod,initialState,game):
        if(usedSearchMethod == 'BPA'):
            return Bfs(initialState,game)
        elif(userSearchMethod== 'BPP'):
            return Dfs(initialState,game)
        else:
            return LocalHeuristic(initialState,game)