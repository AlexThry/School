class Node:
  def __init__(self, number, au_plus_tot, au_plus_tard, arcs_entrants, arcs_sortants):
    
    assert isinstance(number, int), 'number must be of type "int"'
    assert isinstance(au_plus_tot, int), 'au_plus_tot must be of type "int"'
    assert isinstance(au_plus_tard, int), 'au_plus_tard must be of type "int"'
    
    
    self.number = number
    self.au_plus_tot = au_plus_tot
    self.au_plus_tard = au_plus_tard
    
  def get_au_plus_tot(self) -> int:
    return self.au_plus_tot
  
  def get_au_plus_tard(self) -> int:
    return self.au_plus_tard
  
  def get_number(self) -> int:
    return self.number
  
  def get_next_step(self):
    pass
     
  
