from searchAlgorithms.bfs import Bfs
from searchAlgorithms.dfs import Dfs

class SearchHelper:

    def getSearchMethod(self,usedSearchMethod,initialState,game):
        if(usedSearchMethod == 'BPA'):
            return Bfs(initialState,game)
        else:
            return Dfs(initialState,game)
