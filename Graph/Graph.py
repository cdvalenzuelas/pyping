from Graph.Graph_Utils import find_one_node_element, find_two_nodes_elements, next_node
from element_classes.Pipe import Pipe
from element_classes.RedConc import RedConc
from element_classes.Reservory import Reservory
from element_classes.RedExc import RedExc
from element_classes.Elbow import Elbow
from element_classes.Flange import Flange
from element_classes.Sprinkler import Sprinkler


class Graph:
  """
    Graph class implement
  """

  def __init__(self, data):    
    self.graph = {}
    self.nodes = data['nodes']
    self.elements = data['elements']
    self.input_node = data['input_node']
    self.output_nodes = data['output_nodes']
    self.create_graph()


  def add_node(self, node_data):
    node = {}
    node_id = node_data['id']
    node_type = node_data['type']

    del node_data['id']
    del node_data['type']   

    node['fathers'] = []
    node['children'] = []     

    if node_type == 'PIPE':
      node['element'] = Pipe(node_data, fluid_dict={'rho': 1000})
    elif node_type == 'ELBOW':
      node['element'] = Elbow(node_data, fluid_dict={'rho': 1000})
    elif node_type == 'RED_CONC':
      node['element'] = RedConc(node_data, fluid_dict={'rho': 1000})
    elif node_type == 'FLANGE':
      node['element'] = Flange(node_data, fluid_dict={'rho': 1000})
    elif node_type == 'RED_EXC':
      node['element'] = RedExc(node_data, fluid_dict={'rho': 1000})
    elif node_type == 'RESERVORY':
      node['element'] = Reservory(node_data)
    elif node_type == 'SPRINKLER':
      node['element'] = Sprinkler(node_data, fluid_dict={'rho': 1000})

    self.graph[node_id] = node

  def create_graph(self):
    """
      Describe the element's order
    """

    input_node = self.input_node
    output_nodes = self.output_nodes
    nodes = self.nodes
    elements = self.elements

    output_node = None
    output_nodes_compare = []

    while output_nodes != output_nodes_compare:  
      element = None

      #Find a element wich has one node (se debe optimizar)
      try:
        element, index = find_one_node_element(elements=elements, node = input_node)

        if element == None:
          raise KeyError    

        if input_node in output_nodes:
          output_nodes_compare.append(input_node)        
        
        self.add_node(element)      
        output_node = next_node(node=input_node, nodes=nodes)      
        elements.pop(index)      
        nodes.pop(input_node)
        continue
      except KeyError:
          pass

      #Find a element wich has two nodes (se debe optimizar)
      try:         
        element, index = find_two_nodes_elements(elements=elements, input_node=input_node, output_node=output_node)         

        if element == None:
          raise KeyError
        
        self.add_node(element)
        input_node = output_node
        output_node = next_node(node=input_node, nodes=nodes)           
        nodes.pop(input_node)
        elements.pop(index)
        continue
      except KeyError:
          pass


    
    