"""
Defines underlying structure of individual nodes, edges and overall network

"""

import numpy as np

# class of total network / consists of links and nodes 
# initialize network cost and update according to BPR function  
class Network:
    def __init__(self, netname):
        self.name = netname
        self.edge_id_set = set()
        self.edgeset = {}
        self.edgefullset={}
        self.edgenode = {}
        self.node_id_set = set()
        self.nodeset = {}

    def add_edge(self, edge):
        self.edge_id_set.add(edge.id)
        self.edgeset[edge.id] = edge
        self.edgefullset[(edge.pointer.id,edge.pointee.id)] = edge
        self.edgenode[(edge.pointer.id, edge.pointee.id)] = edge.id
        if edge.pointer.id not in self.node_id_set:
            node = Vertex(edge.pointer)
            node.heads.append(edge)
            self.nodeset[edge.pointer.id] = node
            self.node_id_set.add(edge.pointer.id)
        else:
            self.nodeset[edge.pointer.id].heads.append(edge)
        if edge.pointee.id not in self.node_id_set:
            node = Vertex(edge.pointee)
            node.tails.append(edge)
            self.nodeset[edge.pointee.id] = node
            self.node_id_set.add(edge.pointee.id)
        else:
            self.nodeset[edge.pointee.id].tails.append(edge)

    def init_cost(self):
        volume = {}
        for l in self.edge_id_set:
            volume[l] = 0
        self.update_cost(volume)

    def update_cost(self, volume):
        for l in self.edgeset.keys():
            self.edgeset[l].cal_costs(volume[l])


# class of links / edges in network 
# includes all major attributes of link-capacity, freeflow travel time, BPR alpha/ beta, costs..
class Edge:
    def __init__(self, edge_info):
        self.id = edge_info[0]
        self.pointer = Vertex(edge_info[1])
        self.pointee = Vertex(edge_info[2])
        self.fft = float(edge_info[3])
        self.capacity = float(edge_info[4])
        self.alpha = float(edge_info[5])
        self.beta = float(edge_info[6].strip())
        self.cost = float('inf')
        self.volume = 0

    # calculate costs according to BPR-cost function 
    def cal_costs(self, volume):
        self.cost = self.fft*(1+self.alpha*np.power(volume/self.capacity, self.beta))
        return self.cost


# class of individual nodes / vertices
class Vertex:
    def __init__(self, node_id):
        self.id = node_id
        self.tails = []
        self.heads = []
        self.prev = None
      
