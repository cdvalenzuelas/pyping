import numpy as np

class Sprinkler:
  """
    Sprinkler class implement
  """

  def __init__(self, sprinkler_dict, fluid_dict = {}):
    self.K = sprinkler_dict['K']
    self.node = sprinkler_dict['node']
    self.P = 0
    self.Q_1 = 0
    self.Q_2 = 0
    self.Q_req = sprinkler_dict['Q'][0]
    self.Q_min = sprinkler_dict['Q'][1]
    self.Q_max = sprinkler_dict['Q'][2]
    self.P_min = sprinkler_dict['P'][0]
    self.P_max = sprinkler_dict['P'][1]
  
  def get_info(self, P, Q):
    self.P = P
    self.Q_1 = Q
    error = 0

    if self.P_min and  P < self.P_min:      
      return { 'error': 'Pressure below of minimum working pressure' }
    elif self.P_max and P > self.P_max:      
      return { 'error': 'Pressure above of maximum working pressure' }

    if self.K:
      tolerance = 1
      low_tolerance = 1 - tolerance / 100
      hihg_tolerance = 1 + tolerance /100

      self.Q_2 = self.K * np.sqrt(P)

      if self.Q_min and self.Q_2 < self.Q_min:
        return { 'error': 'Caudal below of minimum required caudal' }
      elif self.Q_max and self.Q_2 > self.Q_max:
        return { 'error': 'Caudal above of maximum required caudal' }

      if self.Q_2 <= self.Q_1 * low_tolerance:        
        return { 'error': 'Caudal is above of high tolerance' }
      elif self.Q_2 >= self.Q_1 * hihg_tolerance:
        return { 'error': 'Caudal is below of low tolerance' }

      return { 'Q': self.Q_2, 'error': None }
    elif self.Q_req:
      self.Q_2 = self.Q_req
      self.K = self.Q_req / np.sqrt(P)
      return { 'Q': self.Q_2, 'error': None }

    

    