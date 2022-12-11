from src.Class_Step import *

class Task:
  def __init__(self, name, duration, connection):
    
    assert isinstance(name, (str, int)), 'name must be of type "str" or "int"'
    assert isinstance(duration, int), 'duration must be of type "int"'
    
    self.name = name
    self.duration = duration
    self.connection = connection #une liste contenant des tuples de la forme (etape_precedante, etape_suivante)
    
  def __str__(self):
    return self.name
  
  def get_name(self) -> str:
    """renvoie le nom de la tâche

    Returns:
        str: nom de la tâche
    """
    return self.name
  
  def get_duration(self) -> int:
    """renvoie la durée de la tâche

    Returns:
        int: durée de la tâche
    """
    return self.duration
  
  
    
  def get_connection(self, str=False) -> tuple:
    """permet de récupérer les étapes à laquelle une tâche est connectée

    Args:
        str (bool, optional): choisis si l'on renvoit le nom des étapes. Defaults to False.

    Returns:
        tuple: les étapes connectées par la tâche
    """
    if str:
      if self.connection:
        connection = (self.connection[0].get_number(), self.connection[1].get_number())
    else:
      if self.connection:
        connection = (self.connection[0], self.connection[1])
    return connection
  
  def get_begin_step(self, str=False):
    """permet de récupérer l'étape dont la tâche sort

    Args:
        str (bool, optional): choisis si l'on renvoit le nom des étapes. Defaults to False.

    Returns:
        l'étape précédente 
    """
    previous_steps = []
    if str:
      if self.connection[0]:
        next_steps = [self.connection[0].get_number()]
    else:
      if self.connection[0]:
        next_steps = [self.connection[0]]
    return next_steps
  
  def get_end_step(self, str=False) -> list:
    """permet de récupérer l'étape suivant la tâche

    Args:
        str (bool, optional): choisis si l'on renvoit le nom des étapes. Defaults to False.

    Returns:
        l'étape suivante
    """
    next_steps = []
    if str:
      if self.connection[1]:
        next_steps += [self.connection[1].get_number()]
    else:
      if self.connection[1]:
        next_steps += [self.connection[1]]
    return next_steps
  

    
    
    
    
    
  