def bernoulli(element):
  if element['type'] == 'PIPE':
    print(element['type'])
    #node_1, x_1, y_1, z_1, intake_1, discharge_1 = element['node_1']
    #node_2, x_2, y_2, z_2, intake_2, discharge_2 = element['node_2']
    #element['length'] = np.sqrt((x_2-x_1)**2 + (y_2 - y_1)**2 + (z_2 - z_1)**2)
  elif element['type'] == 'SPRINKLER':
    if element['K']:
      print(element['type'])
  elif element['type'] == 'RESERVORY':
     print(element['type'])