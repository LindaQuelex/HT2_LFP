
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'INITIALcorchete_abierto corchete_cerrado letras numeros parentesis_abierto parentesis_cerrado\n    INITIAL : corchete_abierto EXPRESIONES corchete_cerrado\n            | parentesis_abierto EXPRESIONES parentesis_cerrado\n            | EXPRESIONES\n    \n    EXPRESIONES : EXPRESIONES INSTRUCCIONES\n           | INSTRUCCIONES\n    \n    INSTRUCCIONES : numeros\n         | letras\n         | corchete_abierto EXPRESIONES corchete_cerrado\n         | parentesis_abierto EXPRESIONES parentesis_cerrado\n    '
    
_lr_action_items = {'corchete_abierto':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[2,8,8,8,-5,-6,-7,8,8,8,-4,8,8,-8,8,-9,-8,-9,]),'parentesis_abierto':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[4,10,10,10,-5,-6,-7,10,10,10,-4,10,10,-8,10,-9,-8,-9,]),'numeros':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[6,6,6,6,-5,-6,-7,6,6,6,-4,6,6,-8,6,-9,-8,-9,]),'letras':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[7,7,7,7,-5,-6,-7,7,7,7,-4,7,7,-8,7,-9,-8,-9,]),'$end':([1,3,5,6,7,11,14,16,17,18,],[0,-3,-5,-6,-7,-4,-1,-2,-8,-9,]),'corchete_cerrado':([5,6,7,9,11,13,17,18,],[-5,-6,-7,14,-4,17,-8,-9,]),'parentesis_cerrado':([5,6,7,11,12,15,17,18,],[-5,-6,-7,-4,16,18,-8,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INITIAL':([0,],[1,]),'EXPRESIONES':([0,2,4,8,10,],[3,9,12,13,15,]),'INSTRUCCIONES':([0,2,3,4,8,9,10,12,13,15,],[5,5,11,5,5,11,5,11,11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INITIAL","S'",1,None,None,None),
  ('INITIAL -> corchete_abierto EXPRESIONES corchete_cerrado','INITIAL',3,'p_INITIAL','analizador.py',56),
  ('INITIAL -> parentesis_abierto EXPRESIONES parentesis_cerrado','INITIAL',3,'p_INITIAL','analizador.py',57),
  ('INITIAL -> EXPRESIONES','INITIAL',1,'p_INITIAL','analizador.py',58),
  ('EXPRESIONES -> EXPRESIONES INSTRUCCIONES','EXPRESIONES',2,'p_EXPRESIONES','analizador.py',73),
  ('EXPRESIONES -> INSTRUCCIONES','EXPRESIONES',1,'p_EXPRESIONES','analizador.py',74),
  ('INSTRUCCIONES -> numeros','INSTRUCCIONES',1,'p_INSTRUCCIONES','analizador.py',85),
  ('INSTRUCCIONES -> letras','INSTRUCCIONES',1,'p_INSTRUCCIONES','analizador.py',86),
  ('INSTRUCCIONES -> corchete_abierto EXPRESIONES corchete_cerrado','INSTRUCCIONES',3,'p_INSTRUCCIONES','analizador.py',87),
  ('INSTRUCCIONES -> parentesis_abierto EXPRESIONES parentesis_cerrado','INSTRUCCIONES',3,'p_INSTRUCCIONES','analizador.py',88),
]
