from tree import Node , Tree
from collections import deque
class Dfs:
    
  
    def __init__(self,initialState,game):
        self.tree = Tree(initialState)
        self.game = game
        self.frontierNodes= deque()
        self.exploredStates= set()
        self.expandedNodesCount = 0
        self.frontierNodesCount = 1

    
    def start(self):
        self.frontierNodes.append(self.tree.root)
        ## Chequeamos el caso especial de que la raiz sea solucion
        if(self.tree.root.state.isGoal):
            solution = self.returnSolutionIterative(self.tree.root)
            return [self.tree,solution]
        while len(self.frontierNodes)>0:
            ## Extraer el primer node n de F (frontierNodes)
            node = self.frontierNodes.pop()
            ## Si n no esta en los explorados, agregarlo
            if(not node.state in self.exploredStates):
                self.exploredStates.add(node.state)
                ## Expandir el nodo n, guardando los sucesores en F y en A
                self.expandedNodesCount+=1
                possibleMoves = self.game.possibleMoves(node.state)
                self.frontierNodesCount-=1
                for move in possibleMoves:
                    self.frontierNodesCount+=1
                    ##Si el nodo n , no esta en Explorados. Guardo los sucesores en Frontier y en los hijos del nodo
                    auxNode = Node( node , move )
                    if(not auxNode in self.exploredStates):
                        node.addChild(auxNode)
                        self.frontierNodes.append(auxNode)
                    if(auxNode.state.isGoal):
                        solution = self.returnSolutionIterative(auxNode)
                        ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                        return [self.tree,solution]
        return None
                    
                    

    def returnSolution(self ,node ):
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l 

    def returnSolutionIterative(self , node):
        solution = deque()
        while(node != self.tree.root):
            solution.appendleft(node)
            node = node.parent
        solution.appendleft(node)
        return solution

    def getExpandedNodesCount(self):
        return self.expandedNodesCount

    def getFrontierNodesCount(self):
        return self.frontierNodesCount