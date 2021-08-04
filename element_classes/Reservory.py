import numpy as np

class Reservory:
  """
    Reservory class implement
  """

  def __init__(self, reservory_dict):
    self.P = reservory_dict['P']
    self.node = reservory_dict['node']     
    self.Q_min = reservory_dict['Q'][0]
    self.Q_max = reservory_dict['Q'][1]
    self.Q = 0  

  def get_info(self, Q):
    self.Q = Q

    error = None

    if Q < self.Q_min:
      error = 'The Q is less than Q_min'
    elif Q > self.Q_max:
      error = 'The Q is greater than Q_max'
    

    return { 'Q': Q, 'P': self.P, 'error': error} 