from tree import Node, Tree
from collections import deque
import math
class VdfsOptimo:

    def __init__(self,initialState,game , maxHeight , growthFactor):
        self.tree = Tree(initialState)
        self.game = game
        ## altura actual, cota izquierda , cota derecha
        self.maxHeight = maxHeight
        self.actualHeight = maxHeight 
        self.lowHeight = 0
        self.growthFactor = growthFactor
        self.solutionStates = dict() ## <height , State>
        self.exploredStates = dict() ## <State,height>
        self.frontierNodes = deque()
        self.discardedFrontier = deque() ## Los que borre por hmax (hojas no por repetido) 
        self.expandedNodesCount = 0
        self.frontierNodesCount = 1
        self.foundASolution = False

    def start(self):
        self.frontierNodes.append(self.tree.root)
        ## Chequeamos el caso especial de que la raiz sea solucion
        if(self.tree.root.state.isGoal):
            solution = self.returnSolution(self.tree.root)
            return [self.tree,solution]
        return self.fixedHeightSearch()


    def fixedHeightSearch(self ): 
        while len(self.frontierNodes)>0:
            ## Extraer el primer node n de F (frontierNodes)
            node = self.frontierNodes.pop()

            ## Si el nodo no esta explorado, o esta explorado en una profundidad mayor, explorarlo
            if(node.state.isGoal  and node.level <= self.actualHeight):
                self.frontierNodes.appendleft(node)
                return self.restart( True , node)

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
                            self.frontierNodes.append(auxNode)

                    if( goalNode is not None and goalNode.level <= self.maxHeight):
                        ## Devolver la solucion, formada por los arcos entre la raiz n0 y el nodo n en A
                        ## Como se encontro una solucion, se hace restart para buscar con altura maxima menor
                        return self.restart( True , goalNode) 
            else:
               #if(not self.foundASolution and node.level <= self.maxHeight ): ##Posible optimizacion, pero no se vieron mejoras en tiempo de ejecucion
                    self.discardedFrontier.append(node)

        ## Como no se encontro una solucion, se hace restart para buscar con altura maxima mayor
        return self.restart(False)

    def restart(self, found , goalNode = None):
    #discard  [ a  b  c ] por altura estan esperando
    #frontier [ d  e  f ] me quedan para mirar (pero como dfs tienen baja prioridad)
    #nuevo frontier  [ a b c d e f ]  
        self.discardedFrontier += self.frontierNodes ##aca son el mismo objeto
        
        self.frontierNodes = self.discardedFrontier                
        self.discardedFrontier = deque() #aca cambio que discarded apunte a otro objeto


        ##Si encontre una solucion, me fijo si es la optima, en caso de serlo la retorno, caso contrario realizo busqueda binaria
        if (found):
            self.solutionStates[goalNode.level] = goalNode.state
            self.foundASolution = True
            if(self.maxHeight == goalNode.level):
               self.lowHeight += 1
            
            self.maxHeight = goalNode.level #donde esta mi solucion 
                                            #uso el nuevo actual height
            self.actualHeight = math.floor((self.lowHeight + self.maxHeight )/2) #varia el actual

            #Encontre la solucion optima
            if(self.actualHeight <= self.lowHeight): 
                print(self.solutionStates)
                solution = self.returnSolution(goalNode)
                return [self.tree,solution]
            
            
            return self.fixedHeightSearch()

        ##Si no encontre una solucion, y nunca lo hice hasta ahora, muevo mis indices para adelante para buscar mas profundo en el arbol mediante busqueda binaria
        if(not self.foundASolution):
            self.lowHeight = self.actualHeight ##ya se que no hay maximo en la primera parte
            self.actualHeight = self.incrementHeight()
            self.maxHeight = self.actualHeight
            return self.fixedHeightSearch()
        
        ##En caso de haber encontrado una solucion alguna vez, pero yendo para atras en el arbol no encontre ninguna, debo mover la cota menor y la actual para encontrar
        ##la solucion entre la minima y la maxima
        if(not found):
            print(f"not found: actual:{self.actualHeight} , min:{self.lowHeight} , max:{self.maxHeight}")
            self.lowHeight = self.actualHeight
            self.actualHeight = math.ceil((self.lowHeight + self.maxHeight )/2) #varia el actual
            return self.fixedHeightSearch()
            
           
    def incrementHeight(self):
        return self.actualHeight + self.growthFactor
            
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
                