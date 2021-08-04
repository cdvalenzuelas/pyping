import numpy as np

class Flange:
  """
    Flange class implement
  """


  def __init__(self, pipe_dict, fluid_dict):
    self.Id = pipe_dict['Id']
    self.node_1 = pipe_dict['node_1']
    self.node_2 = pipe_dict['node_2']
    self.P_1 = 0
    self.P_2 = 0
    self.Q = 0
    self.h = 0
    self.V = 0
    self.rho = fluid_dict['rho']

  def set_P_2(self):
    z_1 = self.node_1[3]
    z_2 = self.node_2[3]
    self.P_2 = self.P_1 + 9.81 * self.rho * (z_1 - z_2) - self.h

  def set_h(self):
    return 0

  def get_info(self, P_1, Q, V = 0):
    if V:
      self.V = V
    else: 
      self.V = 4 * Q  / ( np.pi * self.Id**2 )

    self.Q = Q
    self.set_h()
    self.P_1 = P_1
    self.set_P_2()

    return { 'Q': self.Q, 'P_2': self.P_2, 'V': self.V   }