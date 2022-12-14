
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CONTAINS DIFF EXCLUDE GET INTERSECT LIGNE NAME OR UNION URLexpression : expression LIGNE expression\n\t| GET URL\n\t| GET URL instruction\n\t| GET NAME\n\t| GET NAME instructioninstruction : instruction OR contrainte\n\t| instruction AND contrainte\n\t| contraintecontrainte : CONTAINS NAME\n\t| EXCLUDE NAME'
    
_lr_action_items = {'GET':([0,3,],[2,2,]),'$end':([1,4,5,6,7,8,11,14,15,16,17,],[0,-2,-4,-1,-3,-8,-5,-9,-10,-6,-7,]),'LIGNE':([1,4,5,6,7,8,11,14,15,16,17,],[3,-2,-4,3,-3,-8,-5,-9,-10,-6,-7,]),'URL':([2,],[4,]),'NAME':([2,9,10,],[5,14,15,]),'CONTAINS':([4,5,12,13,],[9,9,9,9,]),'EXCLUDE':([4,5,12,13,],[10,10,10,10,]),'OR':([7,8,11,14,15,16,17,],[12,-8,12,-9,-10,-6,-7,]),'AND':([7,8,11,14,15,16,17,],[13,-8,13,-9,-10,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,],[1,6,]),'instruction':([4,5,],[7,11,]),'contrainte':([4,5,12,13,],[8,8,16,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression LIGNE expression','expression',3,'p_expression','idule.py',53),
  ('expression -> GET URL','expression',2,'p_expression','idule.py',54),
  ('expression -> GET URL instruction','expression',3,'p_expression','idule.py',55),
  ('expression -> GET NAME','expression',2,'p_expression','idule.py',56),
  ('expression -> GET NAME instruction','expression',3,'p_expression','idule.py',57),
  ('instruction -> instruction OR contrainte','instruction',3,'p_instruction','idule.py',86),
  ('instruction -> instruction AND contrainte','instruction',3,'p_instruction','idule.py',87),
  ('instruction -> contrainte','instruction',1,'p_instruction','idule.py',88),
  ('contrainte -> CONTAINS NAME','contrainte',2,'p_contrainte','idule.py',98),
  ('contrainte -> EXCLUDE NAME','contrainte',2,'p_contrainte','idule.py',99),
]
