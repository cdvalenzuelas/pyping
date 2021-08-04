def find_two_nodes_elements(elements, input_node, output_node):
  """
    Find one element whith the correct two nodes
  """
  element_nodes = (input_node, output_node)
  element2 = None
  index = 0  

  for element in elements:
    try:
      node_1 = element['node_1'][0]
      node_2 = element['node_2'][0]        

      if node_1 in element_nodes and node_2 in element_nodes:
        element2 = element
        break
      else:
        index += 1      
    except KeyError:
      index += 1
      continue  
  
  return (element2, index)


def find_one_node_element(elements, node):
  """
    Find one element whith the correct node
  """

  element2 = None
  index = 0

  for element in elements:
    try:
      node_1 = element['node']        

      if node_1 == node:
        element2 = element
        break
      else:
        index += 1  
    except KeyError:
      index += 1
      continue

  return (element2, index)

def next_node(node, nodes):
  """
    Define the next node in de web
  """
  length = len(nodes[node])

  if length == 1:
    return nodes[node][0]
  elif length == 2:
    internal_nodes = nodes[node]  
    

    for internal_node in internal_nodes:      

      try:    
        founded = nodes[internal_node]
        return internal_node          
      except KeyError:
        continue    