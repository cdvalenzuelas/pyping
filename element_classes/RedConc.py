import numpy as np

class RedConc:
  """
    RedConc class implement
  """
  
  def __init__(self, pipe_dict, fluid_dict):    
    self.node_1 = pipe_dict['node_1']
    self.node_2 = pipe_dict['node_2']
    self.P_1 = 0
    self.P_2 = 0
    self.Q = 0
    self.h = 0
    self.V_1 = 0
    self.V_2 = 0
    self.rho = fluid_dict['rho']  

  def set_P_2(self):
    z_1 = self.node_1[3]
    z_2 = self.node_2[3]
    h = self.h
    V_1 = self.V_1
    V_2 = self.V_2
    rho = self.rho
    P_1 = self.P_1    

    self.P_2 = P_1 + (9.81*rho*(z_1-z_2)) + (0.5*rho*(V_1**2 - V_2**2)) - h

  def set_h(self):
    return 0

  def get_info(self, P_1, Q, V = 0):
    D_1 = self.node_1[4]
    D_2 = self.node_2[4]    

    if V:
      self.V_1 = V
      self.V_2 = V * (D_1 / D_2) ** 2
    else: 
      self.V_1 = 4 * Q  / ( np.pi * D_1**2 )
      self.V_2 = 4 * Q  / ( np.pi * D_2**2 )     

    self.Q = Q
    self.set_h()
    self.P_1 = P_1
    self.set_P_2()

    return { 'Q': self.Q, 'P_2': self.P_2, 'V': self.V_2   }
