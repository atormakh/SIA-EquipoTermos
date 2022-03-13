
from treeGraph import TreeGraph
from tree import Node, Tree
from collections import deque

class LocalHeuristic:
    successorsNodes = deque()
    exploredStates = set()
    expandedNodesCount = 0

    def __init__(self,initialState,game):
        self.tree = Tree(initialState)
        self.game = game

    def start(self):
        treeGraph= TreeGraph()
        self.successorsNodes.append(self.tree.root)
        treeGraph.addNode(self.tree.root)
        #Llamamos al metodo recursivo
        solutionNode = self.__recursiveSearchMethod(self.successorsNodes,treeGraph)
        #Si encontro una solucion la retornamos
        if(solutionNode is not None):
            solution = self.returnSolution(solutionNode)
            treeGraph.show("graph.html")
            # Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
            return solution
        #Sino, retornamos "None"
        return None
    
    def returnSolution(self ,node ):
        if(node == self.tree.root):
            return [node]
        l = self.returnSolution(node.parent)
        l.append(node)
        return l

    def __recursiveSearchMethod(self,conjL,treeGraph):
        conjLSuccessors = deque()
        #Mientras L no este vacia
        while conjL:
            #Considerar al nodo n de L cuyo estado tenga el menor valor de heuristica (Ya estamos removiendo n en caso de ser con retroceso)
            node = conjL.popleft()
            #Si el estado no fue previamente explorado
            if(not node.state in self.exploredStates):
                #Agregamos el estado a exploredStates
                self.exploredStates.add(node.state)
                #Chequeamos si el estado de node es solucion
                if(node.state.isGoal):
                    #En caso de que si, retornamos con exito
                    return node
                # Expandir n de acuerdo a las acciones posibles para el estado que lo etiqueta
                self.expandedNodesCount+=1
                possibleMoves = sorted(self.game.possibleMoves(node.state,True),key=lambda x: x.heuristic)
                # Formar una lista de nodos LSucesores con los nodos obtenidos de la expansion de n
                for move in possibleMoves:
                    auxNode= Node(node,move)
                    conjLSuccessors.append(auxNode)
                    node.addChild(auxNode)
                    treeGraph.addNode(auxNode)
                    treeGraph.addEdge(auxNode,node)
                # LLamar a BusquedaHeuristicaLocal(LSucesores)
                returnedNode = self.__recursiveSearchMethod(conjLSuccessors,treeGraph)
                #Chequeamos si llego a una solucion
                if(returnedNode is not None):
                    #Si llego la retornamos, sino seguimos el loop
                    return returnedNode
        return None

    def getExpandedNodesCount(self):
        return self.expandedNodesCount

    def getFrontierNodesCount(self):
        return 0