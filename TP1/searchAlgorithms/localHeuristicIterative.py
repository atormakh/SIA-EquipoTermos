from treeGraph import TreeGraph
from tree import Node, Tree
from collections import deque

class GlobalHeuristic:
    
    frontierNodes = deque()
    exploredStates = set()
    expandedNodesCount = 0

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
        #Mientras F no este vacia
        while self.frontierNodes:
            #Extraer el primer nodo de F
            node = self.frontierNodes.popleft()
            #Si el estado no fue previamente explorado
            if(not node.state in self.exploredStates):
                # Expandir el nodo n, insertando en A y en F, y ordenando esta ultima segun la heuristica utilizada
                self.expandedNodesCount+=1
                possibleMoves = sorted(self.game.possibleMoves(node.state,True),key=lambda x: x.heuristic,reverse=True)
                for move in possibleMoves:
                    auxNode= Node(node,move)
                    self.frontierNodes.append(auxNode)
                    node.addChild(auxNode)
                    treeGraph.addNode(auxNode)
                    treeGraph.addEdge(auxNode,node)
                    if(auxNode.state.isGoal):
                        #Fin de busqueda con exito.
                        solution = self.returnSolution(auxNode)
                        treeGraph.show("graph.html")
                        ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                        return solution


    def returnSolution(self ,node ):
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l

    def getExpandedNodesCount(self):
        return self.expandedNodesCount

    def getFrontierNodesCount(self):
        return 0   