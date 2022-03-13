from treeGraph import TreeGraph
from tree import Node , Tree
from collections import deque
class Bfs:
    frontierNodes= deque()
    exploredStates= set()
    expandedNodesCount = 0
    frontierNodesCount = 1
    
    def __init__(self,initialState,game):
        self.tree = Tree(initialState)
        self.game = game
    
    def start(self):
        treeGraph= TreeGraph()
        self.frontierNodes.append(self.tree.root)
        treeGraph.addNode(self.tree.root)
        ## Chequeamos el caso especial de que la raiz sea solucion
        if(self.tree.root.state.isGoal):
            solution = self.returnSolution(self.tree.root)
            treeGraph.show("graph.html")
            return solution
        while len(self.frontierNodes)>0:
            ## Extraer el primer node n de F (frontierNodes)
            node = self.frontierNodes.popleft()
            ## Si n no esta en los explorados, agregarlo
            if(not node.state in self.exploredStates):
                self.exploredStates.add(node.state)
                ## Si n esta etiquetado con un estado objetivo
          
                ## Expandir el nodo n, guardando los sucesores en F y en A
                self.expandedNodesCount+=1
                possibleMoves = self.game.possibleMoves(node.state)
                self.frontierNodesCount-=1
                for move in possibleMoves:
                    self.frontierNodesCount+=1
                    ##Si el nodo n , no esta en Explorados. Guardo los sucesores en Frontier y en los hijos del nodo
                    auxNode = Node( node , move )
                    if(not auxNode in self.exploredStates):
                        treeGraph.addNode(auxNode)
                        treeGraph.addEdge(node,auxNode)
                        node.addChild(auxNode)
                        self.frontierNodes.append(auxNode)

                    if(auxNode.state.isGoal):
                        solution = self.returnSolution(node)
                        treeGraph.show("graph.html")
                        ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                        return solution 
                 
                  
                   
        return None
                    
                    

    def returnSolution(self ,node ):
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l

    def getExpandedNodesCount(self):
        return self.expandedNodesCount

    def getFrontierNodesCount(self):
        return self.frontierNodesCount