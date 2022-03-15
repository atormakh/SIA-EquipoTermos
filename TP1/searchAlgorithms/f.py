from tree import Node, Tree
from collections import deque
import bisect
class F:
   
    def __init__(self,initialState,game,weight):
        self.tree = Tree(initialState)
        self.game = game
        self.weight=weight
        self.frontierNodes = []
        self.exploredStates = set()
        self.expandedNodesCount = 0
        self.frontierNodesCount = 1
    

    def f(self,node):
        return (1-self.weight)* node.level + self.weight*node.state.heuristic
    
    def start(self):
        self.frontierNodes.append(self.tree.root)
        ## Chequeamos el caso especial de que la raiz sea solucion
        if(self.tree.root.state.isGoal):
            solution = self.returnSolution(self.tree.root)
            return [self.tree,solution]
        while self.frontierNodes:
            ## Extraer el primer node n de F (frontierNodes)
            node = self.frontierNodes.pop()
            ## Si n no esta en los explorados, agregarlo
            if(not node.state in self.exploredStates):
                self.exploredStates.add(node.state)
                ## Expandir el nodo n, guardando los sucesores en F y en A
                self.expandedNodesCount+=1
                possibleMoves = self.game.possibleMoves(node.state,True)
                self.frontierNodesCount-=1
                for move in possibleMoves:
                    self.frontierNodesCount+=1
                    ##Si el nodo n , no esta en Explorados. Guardo los sucesores en Frontier y en los hijos del nodo
                    auxNode = Node( node , move )
                    if(not auxNode in self.exploredStates):
                        node.addChild(auxNode)
                        self.insertOrdered(auxNode)

                    if(auxNode.state.isGoal):
                        solution = self.returnSolution(auxNode)
                        ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                        return [self.tree,solution]       
        return [None, None]
    
    def returnSolution(self ,node ):
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l

    def insertOrdered(self,node):
        bisect.insort(self.frontierNodes,node,key=lambda x: -self.f(x))

    def getExpandedNodesCount(self):
        return self.expandedNodesCount

    def getFrontierNodesCount(self):
        return self.frontierNodesCount