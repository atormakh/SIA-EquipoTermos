
from treeGraph import TreeGraph
from tree import Node, Tree
from collections import deque

import math
class Vdfs:

    exploredStates = dict() ## <State,heigth>
    frontierNodes = deque()
    discardedFrontier = deque() ## Los que borre por hmax (hojas no por repedito) 
    expandedNodesCount = 0
    frontierNodesCount = 1
    foundASolution = False

    def __init__(self,initialState,game , maxHeight):
        self.tree = Tree(initialState)
        self.game = game
        ## altura actual, cota izquierda , cota derecha
        self.actualHeight = maxHeight 

    def start(self):
        treeGraph= TreeGraph()
        self.frontierNodes.append(self.tree.root)
        treeGraph.addNode(self.tree.root)
        ## Chequeamos el caso especial de que la raiz sea solucion
        if(self.tree.root.state.isGoal):
            solution = self.returnSolutionIterative(self.tree.root)
            treeGraph.show("graph.html")
            return solution

        while(not self.foundASolution):
            #print(f"actual:{self.actualHeight} , min:{self.lowHeight} , max:{self.maxHeight}")
            while len(self.frontierNodes)>0:
                ## Extraer el primer node n de F (frontierNodes)
                node = self.frontierNodes.popleft()

                ## Si el nodo no esta explorado, o esta explorado en una profundidad mayor, explorarlo
                if(node.state.isGoal  and node.level <= self.actualHeight):
                    self.foundASolution = True
    
                    solution = self.returnSolutionIterative(goalNode)
                    treeGraph.show("graph.html")
                    return solution

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
                                #treeGraph.addNode(auxNode)
                                #treeGraph.addEdge(node,auxNode)
                                node.addChild(auxNode)
                                if(goalNode is None and auxNode.state.isGoal):
                                    goalNode = auxNode
                                self.frontierNodes.appendleft(auxNode)

                        if( goalNode is not None and goalNode.level <= self.maxHeight):
                            ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                            ## Como se encontro una solucion, se hace restart para buscar con altura maxima menor
                            self.foundASolution = True
                     
                            solution = self.returnSolutionIterative(goalNode)
                            treeGraph.show("graph.html")
                            return solution

                else:
                        self.discardedFrontier.appendleft(node)
                        
            print("resetting frontier")
            self.resetFrontier()
            self.actualHeight = self.incrementHeight()
            self.maxHeight = self.actualHeight
            print(f"mi altura {self.maxHeight}")
        

    def resetFrontier(self):
        self.discardedFrontier += self.frontierNodes ##aca son el mismo objeto
        self.frontierNodes = self.discardedFrontier                
        self.discardedFrontier = deque() #aca cambio que discarded apunte a otro objeto
        print(f"En frontier nodes {len(self.frontierNodes)}")
           
    def incrementHeight(self):
        return math.ceil(self.actualHeight * 1.25) ##sqrt(2)
            
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
                
