from src.Class_Node import *

class Arc:
  def __init__(self, name, duration, node1, node2):
    
    assert isinstance(name, (str, int)), 'name must be of type "str" or "int"'
    assert isinstance(duration, int), 'duration must be of type "int"'
    assert isinstance(node1, Node), 'node1 must be of type "Node"'
    assert isinstance(node2, Node), 'node2 must be of type "Node"'
    
    self.name = name
    self.duration = duration
    self.node1 = node1
    self.node2 = node2
    
    
  