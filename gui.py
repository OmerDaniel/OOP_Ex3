from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from MyGraphAlgo import MyGraphAlgo
import networkx as nx
from MyGraph import MyGraph
if __name__ == '__main__':
    g = MyGraph({}, {}, 0)
    graph = MyGraphAlgo(g)
    print("enter your json graph file path here:")
    s = input()   #like : C:\\Users\\omer\\PycharmProjects\\Ex3\\data\\A0.json
    str(s)
    graph.load_from_json(s)
    xv = []
    yv = []
    id=[]
    x = graph.graph.get_all_v()
    for i in x.values():
        xv.append(i.x)
        yv.append(i.y)
        id.append(i.id)
    points = []
    pos = {}
    for i in range(len(xv)):
        point = (float(xv[i]),float(yv[i]))
        points.append(point)
        pos[id[i]]=point
    edges = []
    for i in range(graph.graph.v_size()):
        d = graph.graph.all_out_edges_of_node(i)
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
    nx.draw_networkx(G, pos, **options)

    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()

