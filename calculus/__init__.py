from elements import elements
from nodes import nodes
from bernoully import bernoulli
from iter_nodes import iter_nodes

outputs = [7] #Debe venir antes de los cálculos
inputs = [1] #Debe venir antes de los cálculos
requirements = (0) #Describe si el requerimiento de las salidas se ha cumplido, si se cumple se para el script

input_elements = list(filter(lambda element: element['type'] in ['RESERVORY', 'PUMP'], elements)) #Trae las bombas y los reservorios
Q_0_min, Q_0_max  = input_elements[0]['Q'] #Presiones de la fuente de presión
P_0 = input_elements[0]['P']
Q_0 = (Q_0_max + Q_0_min) / 2
node = inputs[0]


iter_nodes(input_node=node, output_nodes=outputs, nodes=nodes, elements=elements)



#for node_key in nodes:
#  print(nodes[node_key])

#for element in elements:
#  bernoulli(element)