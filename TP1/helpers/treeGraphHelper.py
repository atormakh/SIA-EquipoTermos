from collections import deque
from pyvis.network import Network
import json
class TreeGraphHelper:
    colors=['#e4cfea', '#be93e9', '#bc93dd', '#9856c8']
    winColor='#7fe4b4'
    exploredNodes=[]
    frontierNodes=deque()
    edges=[]
    def __init__(self,tree,solution , counter):
        self.network= Network()
        with open('./config/network_options.txt') as f:
            lines = f.read()
        self.network.set_options(lines)
        #JODITA
        self.frontierNodes.append(tree.root)
        while self.frontierNodes:
            currentNode=self.frontierNodes.pop()
            currentNodeHash=hash(currentNode)
            self.exploredNodes.append(currentNode)
            if(len(currentNode.children)>0):
                self.frontierNodes.extend(currentNode.children)
            for auxNode in currentNode.children:
                self.edges.append((currentNodeHash,hash(auxNode)))
        
        self.addNodes(self.exploredNodes)
        self.addEdges(self.edges)
        self.show(f"./results/graphs/graph{counter}.html")
            
        
    def addNodes(self,nodes):
        nodeIds=list(map(lambda x:hash(x),nodes))
        titles=list(map(lambda x:str(x.state),nodes))
        labels=list(map(lambda x: x.level,nodes))
        colors=list(map(lambda x:(self.winColor if x.state.isGoal else self.colors[x.level%4]),nodes))
        self.network.add_nodes(nodeIds,title=titles,label=labels,color=colors)        

    def addEdges(self,edges):
        self.network.add_edges(edges)

    def addNode(self,node,options={}):
        self.network.add_node(hash(node),physics=True,title=str(node.state),label=node.level,level=node.level,y=node.level*100,color=(self.winColor if node.state.isGoal else self.colors[node.level%4]))

    def addEdge(self,node1,node2,options={}):
        self.network.add_edge(hash(node1),hash(node2))

    def show(self,filename):
        self.network.show(filename)