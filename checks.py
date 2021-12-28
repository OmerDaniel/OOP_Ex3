import sys

from MyNode import MyNode
from MyGraph import MyGraph
from MyEdges import MyEdges
from MyGraphAlgo import MyGraphAlgo
import json
if __name__ == '__main__':
    g=MyGraph({},{},0)
    s=""#enter the file path here (example : C:\\Users\\omer\\PycharmProjects\\Ex3\\data\\A0.json)
    algo = MyGraphAlgo(g)
    algo.load_from_json(s)






