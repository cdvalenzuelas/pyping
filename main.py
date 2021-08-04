from Graph.Graph import Graph
from elements import elements
from nodes import nodes
import json

data = {
  'elements': elements,
  'nodes': nodes,
  'input_node': 1,
  'output_nodes': [7]
}


#from create_main_csv import create_main_csv

if __name__ == '__main__':
   my_graph = Graph(data=data)   
   print(my_graph.graph[3]['element'].get_info(Q=100))

