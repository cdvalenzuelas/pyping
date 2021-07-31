next_node = None

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

def iter_nodes(input_node, output_nodes, nodes, elements):
  """
    Describe the element's order
  """

  output_node = None
  output_nodes_compare = []

  while output_nodes != output_nodes_compare:  
    element = None

    #Find a element wich has one node
    try:
      element, index = find_one_node_element(elements=elements, node = input_node)

      if element == None:
        raise KeyError    

      if input_node in output_nodes:
        output_nodes_compare.append(input_node)        
      
      print(element)
      output_node = next_node(node=input_node, nodes=nodes)      
      elements.pop(index)      
      nodes.pop(input_node)
      continue
    except KeyError:
        pass

    #Find a element wich has two nodes
    try:         
      element, index = find_two_nodes_elements(elements=elements, input_node=input_node, output_node=output_node)         

      if element == None:
        raise KeyError
      
      print(element)
      input_node = output_node
      output_node = next_node(node=input_node, nodes=nodes)           
      nodes.pop(input_node)
      elements.pop(index)
      continue
    except KeyError:
        pass




    