import random

from GraphInterface import GraphInterface
from MyNode import MyNode
from MyEdges import MyEdges
class MyGraph (GraphInterface):
    def __init__(self,points={},edges={},mc=0):
        self.points=points
        self.edges=edges
        self.mc=mc

    def v_size(self) -> int:
        a=len(self.points)
        return a

    def e_size(self) -> int:
        answer =0
        for values in self.edges.values():
            answer+=len(values)
        return answer
    def getedges (self):
        return self.edges
    def get_all_v(self) -> dict:
        return self.points

    def all_in_edges_of_node(self, id1: int) -> dict:
        a = {}
        for i in self.edges[id1].values():
            a[i.dest] = i.wheight
        return a

    def all_out_edges_of_node(self, id1: int) -> dict:
        a={}
        for i in self.edges[id1].values():
            a[i.dest]=i.wheight
        return a

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.points:
            return False
        if id2 not in self.points:
            return False
        if id1 in self.edges:
          if id2 not in self.edges[id1]:
            a=MyEdges(id1,id2,weight)
            d=self.edges[id1]
            d[id2]=a
            self.mc=self.mc+1
            self.points[id2].d[id1]=a.wheight
            self.points[id2].destedge.append(id1)
            self.mc = self.mc + 1
            return True
        return

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.points:
            return
        else:
            if pos is None:
                pos=[random.randint(1,100),random.randint(1,100)]
            a = MyNode(pos[0], pos[1], 0, node_id, 0)
            self.points[node_id] = a
            self.edges[node_id] = {}
            self.mc = self.mc + 1
            return True


    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.points:
           return
        for i in self.points[node_id].destedge:
            self.edges[i][node_id]=None
        self.points[node_id]=None
        self.mc=self.mc+1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.edges:
            if node_id2 in self.edges[node_id1]:
                self.edges[node_id1][node_id2] = None
                self.edges[node_id1]
                self.mc = self.mc + 1
                return True
        return




