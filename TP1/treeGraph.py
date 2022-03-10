from pyvis.network import Network
import json
class TreeGraph:
    colors=['#e4cfea', '#be93e9', '#bc93dd', '#9856c8']
    winColor='#7fe4b4'
    def __init__(self):
        self.network= Network()
        with open('./config/network_options.txt') as f:
            lines = f.read()
        self.network.set_options(lines)

    def addNode(self,node,options={}):
        self.network.add_node(hash(node),physics=True,title=str(node.state),label=node.level,level=node.level,y=node.level*100,color=(self.winColor if node.state.isGoal else self.colors[node.level%4]))

    def addEdge(self,node1,node2,options={}):
        self.network.add_edge(hash(node1),hash(node2))

    def show(self,filename):
        self.network.show(filename)

                