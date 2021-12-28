import json
import sys
from typing import List

import networkx as nx
from matplotlib import pyplot as plt

import GraphInterface
from MyGraph import MyGraph
from GraphAlgoInterface import GraphAlgoInterface


class MyGraphAlgo(GraphAlgoInterface):
    def __init__(self, graph=MyGraph):
        self.graph = graph
    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as f:
                dict_graph = json.load(f)
                nodes = dict_graph.get("Nodes")
                edges = dict_graph.get("Edges")
                for values in nodes:
                    pos = (values.get("pos")).split(",")
                    self.graph.add_node(values.get("id"), pos)
                for values in edges:
                    self.graph.add_edge(values.get("src"), values.get("dest"), values.get("w"))
        except FileExistsError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as f:
                f.write("{\n")
                f.write("\"Edges\":[\n")
                counter = 0
                for k in self.graph.getedges().values():
                    for i in k.values():
                     f.write("{\n")
                     f.write("\"src\":"+str(i.src)+",\n")
                     f.write("\"w\":"+str(i.wheight)+",\n")
                     f.write("\"dest\":" + str(i.dest)+"\n")
                     print (str(counter)+","+str(self.graph.e_size()))
                     if (counter+1 == self.graph.e_size()):
                         f.write("}\n")
                         counter += 1
                     else:
                         f.write("},\n")
                         counter += 1
                f.write("],"+"\n")
                f.write("\"Nodes\": [\n")
                for i in self.graph.get_all_v().values():
                    f.write("{\n")
                    f.write("\"pos\":\""+str(i.x)+","+str(i.y)+","+str(i.z)+"\",\n")
                    f.write("\"id\":" + str(i.id) +"\n")
                    if (i.id+1==self.graph.v_size()):
                        f.write("}\n")
                    else:
                        f.write("},\n")
                f.write("]" + "\n")
                f.write("}\n")







        except FileExistsError as e:
            print(e)



    def shortest_path(self, id1: int, id2: int) -> (float, list):
        totalsize=self.graph.v_size()
        visited=[]
        gothereby=[]
        gotherewheight=[]
        for i in range(totalsize):
            visited.append(False)
            gothereby.append(-1)
            gotherewheight.append(sys.maxsize)
        gotherewheight[id1]=0
        unimportantindex=0
        while(unimportantindex<totalsize):
            minimumofshortestwheight=sys.maxsize
            shortesttorootunvisited=-1
            for k in range(totalsize):
                if(not visited[k] and gotherewheight[k]<minimumofshortestwheight):
                    minimumofshortestwheight=gotherewheight[k]
                    shortesttorootunvisited=k
            d=self.graph.getedges().get(shortesttorootunvisited)
            for value in d.values():
                neighboredge=value
                edgedest=neighboredge.dest
                newpossiblewheight=minimumofshortestwheight+neighboredge.wheight
                if(visited[edgedest]):
                    continue
                if(gotherewheight[edgedest]<=newpossiblewheight):
                    continue
                gothereby[edgedest]=shortesttorootunvisited
                gotherewheight[edgedest]=newpossiblewheight
            visited[shortesttorootunvisited]=True
            unimportantindex += 1
        pathtodest=[]
        source=id2
        pathtodest.append(id2)
        while(source != id1):
            source=gothereby[source]
            pathtodest.append(source)
        pathtodest.reverse()
        ans=(gotherewheight[id2],pathtodest)
        return ans[1]

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        id = []
        x = self.graph.get_all_v()
        for i in x.values():
            id.append(i.id)
        edges = []
        for i in range(self.graph.v_size()):
            d = self.graph.all_out_edges_of_node(i)
            for k in d:
                edge = (i, k)
                edges.append(edge)
        G = nx.Graph()
        for i in range(len(edges)):
            G.add_edge(edges[i][0], edges[i][1])

        options = {
            "font_size": 36,
            "node_size": 3000,
            "node_color": "white",
            "edgecolors": "black",
            "linewidths": 5,
            "width": 5,
        }
        nx.draw_networkx(G, id, **options)

        ax = plt.gca()
        ax.margins(0.20)
        plt.axis("off")
        plt.show()




