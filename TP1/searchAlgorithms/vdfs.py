from tree import Node, Tree
from collections import deque

import math
class Vdfs:

    

    def __init__(self,initialState,game , maxHeight , growthFactor):
        self.tree = Tree(initialState)
        self.game = game
        ## altura actual, cota izquierda , cota derecha
        self.actualHeight = maxHeight
        self.maxHeight = maxHeight
        self.growthFactor = growthFactor
        self.exploredStates = dict() ## <State,height>
        self.frontierNodes = deque()
        self.discardedFrontier = deque() ## Los que borre por hmax (hojas no por repetidos) 
        self.expandedNodesCount = 0
        self.frontierNodesCount = 1
        self.foundASolution = False

    def start(self):
        self.frontierNodes.append(self.tree.root)
        ## Chequeamos el caso especial de que la raiz sea solucion
        if(self.tree.root.state.isGoal):
            solution = self.returnSolutionIterative(self.tree.root)
            return [self.tree,solution]

        while(not self.foundASolution):
            while len(self.frontierNodes)>0:
                ## Extraer el primer node n de F (frontierNodes)
                node = self.frontierNodes.popleft()

                ## Si el nodo no esta explorado, o esta explorado en una profundidad mayor, explorarlo
                if(node.state.isGoal  and node.level <= self.actualHeight):
                    self.foundASolution = True
    
                    solution = self.returnSolutionIterative(goalNode)
                    return [self.tree,solution]

                if(node.level  < self.actualHeight ):
                    if(not node.state in self.exploredStates or self.exploredStates[node.state] > node.level):
                        self.exploredStates[node.state] = node.level
                        ## Expandir el nodo n, guardando los sucesores en F y en A
                        self.expandedNodesCount+=1
                        possibleMoves = self.game.possibleMoves(node.state)
                        self.frontierNodesCount-=1
                        
                        goalNode = None

                        for move in possibleMoves:
                            self.frontierNodesCount+=1
                            ##Si el nodo n , no esta en Explorados. Guardo los sucesores en Frontier y en los hijos del nodo
                            auxNode = Node( node , move )
                            if(not auxNode in self.exploredStates):
                                node.addChild(auxNode)
                                if(goalNode is None and auxNode.state.isGoal):
                                    goalNode = auxNode
                                self.frontierNodes.appendleft(auxNode)

                        if( goalNode is not None and goalNode.level <= self.maxHeight):
                            ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                            ## Como se encontro una solucion, se hace restart para buscar con altura maxima menor
                            self.foundASolution = True
                     
                            solution = self.returnSolutionIterative(goalNode)
                            return [self.tree,solution]

                else:
                        self.discardedFrontier.appendleft(node)
                        
            self.resetFrontier()
            self.actualHeight = self.incrementHeight()
            self.maxHeight = self.actualHeight
        

    def resetFrontier(self):
        self.discardedFrontier += self.frontierNodes ##aca son el mismo objeto
        self.frontierNodes = self.discardedFrontier                
        self.discardedFrontier = deque() #aca cambio que discarded apunte a otro objeto
     #   print(f"En frontier nodes {len(self.frontierNodes)}")
           
    def incrementHeight(self):
        return self.actualHeight + self.growthFactor 
            
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
                
