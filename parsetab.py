
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOleftYrightNEGleftIGUALDIFERENTEleftMENORMENOR_IGUALMAYORMAYOR_IGUALleftMASMENOSleftPORDIVIDIDOMODULOALGORITMO ASIGNAR CADENA COMA DEFINIR DIFERENTE DIVIDIDO ENTERO ENTONCES ESCRIBIR FALSO FIN FLOTANTE ID IGUAL INICIO MAS MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MENOS MIENTRAS MODULO NEG NUMERO O PARENTESIS_DERECHO PARENTESIS_IZQUIERDO POR PUNTO_Y_COMA SI SINO VERDADERO Yprograma : ALGORITMO ID bloque FIN ALGORITMObloque : declaraciones INICIO instrucciones FINdeclaraciones : DEFINIR lista_ids tipo\n                     | declaraciones DEFINIR lista_ids tipolista_ids : ID\n                 | lista_ids COMA IDtipo : ENTEROinstrucciones : instruccion\n                     | instrucciones instruccioninstruccion : escritura\n                   | asignacion\n                   | mientras\n                   | siasignacion : ID ASIGNAR expresion PUNTO_Y_COMA\n                  | ID ASIGNAR expresionescritura : ESCRIBIR PARENTESIS_IZQUIERDO lista_expr PARENTESIS_DERECHO PUNTO_Y_COMA\n                  | ESCRIBIR PARENTESIS_IZQUIERDO lista_expr PARENTESIS_DERECHOlista_expr : expresion\n                  | lista_expr COMA expresionexpresion : NUMEROexpresion : FLOTANTEexpresion : CADENAexpresion : VERDADERO\n                 | FALSOexpresion : IDexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIVIDIDO expresion\n                  | expresion MODULO expresion\n                  | expresion IGUAL expresion\n                  | expresion DIFERENTE expresion\n                  | expresion MENOR expresion\n                  | expresion MAYOR expresion\n                  | expresion MENOR_IGUAL expresion\n                  | expresion MAYOR_IGUAL expresion\n                  | expresion Y expresion\n                  | expresion O expresionexpresion : NEG expresionexpresion : PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHOmientras : MIENTRAS expresion instrucciones FIN MIENTRASsi : SI expresion ENTONCES instrucciones sino_opcionalsino_opcional : SINO si\n                     | SINO instrucciones\n                     | emptyempty :'
    
_lr_action_items = {'ALGORITMO':([0,7,],[2,12,]),'$end':([1,12,],[0,-1,]),'ID':([2,6,8,9,13,14,15,16,17,18,21,22,25,28,29,30,31,32,33,34,35,36,37,38,39,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,],[3,11,20,11,20,-8,-10,-11,-12,-13,37,37,42,-9,37,37,20,-20,-21,-22,-23,-24,-25,37,37,-15,20,37,37,37,37,37,37,37,37,37,37,37,37,37,-39,20,-17,37,-14,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,20,-16,-41,-42,20,-45,-13,20,]),'DEFINIR':([3,5,24,26,41,],[6,9,-3,-7,-4,]),'FIN':([4,13,14,15,16,17,18,27,28,32,33,34,35,36,37,45,46,60,63,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,87,88,89,],[7,27,-8,-10,-11,-12,-13,-2,-9,-20,-21,-22,-23,-24,-25,-15,66,-39,-17,-14,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,-46,-16,-41,-42,-45,-13,-44,]),'INICIO':([5,24,26,41,],[8,-3,-7,-4,]),'ESCRIBIR':([8,13,14,15,16,17,18,28,31,32,33,34,35,36,37,45,46,60,62,63,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,],[19,19,-8,-10,-11,-12,-13,-9,19,-20,-21,-22,-23,-24,-25,-15,19,-39,19,-17,-14,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,19,-16,-41,-42,19,-45,-13,19,]),'MIENTRAS':([8,13,14,15,16,17,18,28,31,32,33,34,35,36,37,45,46,60,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,],[21,21,-8,-10,-11,-12,-13,-9,21,-20,-21,-22,-23,-24,-25,-15,21,-39,21,-17,-14,84,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,21,-16,-41,-42,21,-45,-13,21,]),'SI':([8,13,14,15,16,17,18,28,31,32,33,34,35,36,37,45,46,60,62,63,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,],[22,22,-8,-10,-11,-12,-13,-9,22,-20,-21,-22,-23,-24,-25,-15,22,-39,22,-17,-14,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,22,-16,-41,-42,22,-45,-13,22,]),'COMA':([10,11,23,32,33,34,35,36,37,42,43,44,60,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[25,-5,25,-20,-21,-22,-23,-24,-25,-6,64,-18,-39,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,-19,]),'ENTERO':([10,11,23,42,],[26,-5,26,-6,]),'SINO':([14,15,16,17,18,28,32,33,34,35,36,37,45,60,63,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,87,88,89,],[-8,-10,-11,-12,-13,-9,-20,-21,-22,-23,-24,-25,-15,-39,-17,-14,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,86,-16,-41,-42,-45,-13,-44,]),'PARENTESIS_IZQUIERDO':([19,21,22,29,30,38,39,47,48,49,50,51,52,53,54,55,56,57,58,59,64,],[29,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'ASIGNAR':([20,],[30,]),'NUMERO':([21,22,29,30,38,39,47,48,49,50,51,52,53,54,55,56,57,58,59,64,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'FLOTANTE':([21,22,29,30,38,39,47,48,49,50,51,52,53,54,55,56,57,58,59,64,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'CADENA':([21,22,29,30,38,39,47,48,49,50,51,52,53,54,55,56,57,58,59,64,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'VERDADERO':([21,22,29,30,38,39,47,48,49,50,51,52,53,54,55,56,57,58,59,64,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'FALSO':([21,22,29,30,38,39,47,48,49,50,51,52,53,54,55,56,57,58,59,64,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'NEG':([21,22,29,30,38,39,47,48,49,50,51,52,53,54,55,56,57,58,59,64,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'MAS':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[47,-20,-21,-22,-23,-24,-25,47,47,47,47,47,-26,-27,-28,-29,-30,47,47,47,47,47,47,47,47,-40,47,]),'MENOS':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[48,-20,-21,-22,-23,-24,-25,48,48,48,48,48,-26,-27,-28,-29,-30,48,48,48,48,48,48,48,48,-40,48,]),'POR':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[49,-20,-21,-22,-23,-24,-25,49,49,49,49,49,49,49,-28,-29,-30,49,49,49,49,49,49,49,49,-40,49,]),'DIVIDIDO':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[50,-20,-21,-22,-23,-24,-25,50,50,50,50,50,50,50,-28,-29,-30,50,50,50,50,50,50,50,50,-40,50,]),'MODULO':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[51,-20,-21,-22,-23,-24,-25,51,51,51,51,51,51,51,-28,-29,-30,51,51,51,51,51,51,51,51,-40,51,]),'IGUAL':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[52,-20,-21,-22,-23,-24,-25,52,52,52,52,52,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,52,52,-40,52,]),'DIFERENTE':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[53,-20,-21,-22,-23,-24,-25,53,53,53,53,53,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,53,53,-40,53,]),'MENOR':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[54,-20,-21,-22,-23,-24,-25,54,54,54,54,54,-26,-27,-28,-29,-30,54,54,-33,-34,-35,-36,54,54,-40,54,]),'MAYOR':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[55,-20,-21,-22,-23,-24,-25,55,55,55,55,55,-26,-27,-28,-29,-30,55,55,-33,-34,-35,-36,55,55,-40,55,]),'MENOR_IGUAL':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[56,-20,-21,-22,-23,-24,-25,56,56,56,56,56,-26,-27,-28,-29,-30,56,56,-33,-34,-35,-36,56,56,-40,56,]),'MAYOR_IGUAL':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[57,-20,-21,-22,-23,-24,-25,57,57,57,57,57,-26,-27,-28,-29,-30,57,57,-33,-34,-35,-36,57,57,-40,57,]),'Y':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[58,-20,-21,-22,-23,-24,-25,58,58,58,-39,58,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,58,-40,58,]),'O':([31,32,33,34,35,36,37,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[59,-20,-21,-22,-23,-24,-25,59,59,59,-39,59,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,59,]),'ENTONCES':([32,33,34,35,36,37,40,60,67,68,69,70,71,72,73,74,75,76,77,78,79,80,],[-20,-21,-22,-23,-24,-25,62,-39,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,]),'PARENTESIS_DERECHO':([32,33,34,35,36,37,43,44,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[-20,-21,-22,-23,-24,-25,63,-18,-39,80,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,-19,]),'PUNTO_Y_COMA':([32,33,34,35,36,37,45,60,63,67,68,69,70,71,72,73,74,75,76,77,78,79,80,],[-20,-21,-22,-23,-24,-25,65,-39,82,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'bloque':([3,],[4,]),'declaraciones':([3,],[5,]),'lista_ids':([6,9,],[10,23,]),'instrucciones':([8,31,62,86,],[13,46,81,89,]),'instruccion':([8,13,31,46,62,81,86,89,],[14,28,14,28,14,28,14,28,]),'escritura':([8,13,31,46,62,81,86,89,],[15,15,15,15,15,15,15,15,]),'asignacion':([8,13,31,46,62,81,86,89,],[16,16,16,16,16,16,16,16,]),'mientras':([8,13,31,46,62,81,86,89,],[17,17,17,17,17,17,17,17,]),'si':([8,13,31,46,62,81,86,89,],[18,18,18,18,18,18,88,18,]),'tipo':([10,23,],[24,41,]),'expresion':([21,22,29,30,38,39,47,48,49,50,51,52,53,54,55,56,57,58,59,64,],[31,40,44,45,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,83,]),'lista_expr':([29,],[43,]),'sino_opcional':([81,],[85,]),'empty':([81,],[87,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> ALGORITMO ID bloque FIN ALGORITMO','programa',5,'p_programa','Sintax_.py',21),
  ('bloque -> declaraciones INICIO instrucciones FIN','bloque',4,'p_bloque','Sintax_.py',26),
  ('declaraciones -> DEFINIR lista_ids tipo','declaraciones',3,'p_declaraciones','Sintax_.py',31),
  ('declaraciones -> declaraciones DEFINIR lista_ids tipo','declaraciones',4,'p_declaraciones','Sintax_.py',32),
  ('lista_ids -> ID','lista_ids',1,'p_lista_ids','Sintax_.py',42),
  ('lista_ids -> lista_ids COMA ID','lista_ids',3,'p_lista_ids','Sintax_.py',43),
  ('tipo -> ENTERO','tipo',1,'p_tipo','Sintax_.py',52),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','Sintax_.py',57),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','Sintax_.py',58),
  ('instruccion -> escritura','instruccion',1,'p_instruccion','Sintax_.py',67),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','Sintax_.py',68),
  ('instruccion -> mientras','instruccion',1,'p_instruccion','Sintax_.py',69),
  ('instruccion -> si','instruccion',1,'p_instruccion','Sintax_.py',70),
  ('asignacion -> ID ASIGNAR expresion PUNTO_Y_COMA','asignacion',4,'p_asignacion','Sintax_.py',75),
  ('asignacion -> ID ASIGNAR expresion','asignacion',3,'p_asignacion','Sintax_.py',76),
  ('escritura -> ESCRIBIR PARENTESIS_IZQUIERDO lista_expr PARENTESIS_DERECHO PUNTO_Y_COMA','escritura',5,'p_escritura','Sintax_.py',81),
  ('escritura -> ESCRIBIR PARENTESIS_IZQUIERDO lista_expr PARENTESIS_DERECHO','escritura',4,'p_escritura','Sintax_.py',82),
  ('lista_expr -> expresion','lista_expr',1,'p_lista_expr','Sintax_.py',89),
  ('lista_expr -> lista_expr COMA expresion','lista_expr',3,'p_lista_expr','Sintax_.py',90),
  ('expresion -> NUMERO','expresion',1,'p_expresion_num','Sintax_.py',100),
  ('expresion -> FLOTANTE','expresion',1,'p_expresion_flota','Sintax_.py',104),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','Sintax_.py',108),
  ('expresion -> VERDADERO','expresion',1,'p_expresion_bool','Sintax_.py',112),
  ('expresion -> FALSO','expresion',1,'p_expresion_bool','Sintax_.py',113),
  ('expresion -> ID','expresion',1,'p_expresion_id','Sintax_.py',117),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','Sintax_.py',122),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','Sintax_.py',123),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','Sintax_.py',124),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_binaria','Sintax_.py',125),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_binaria','Sintax_.py',126),
  ('expresion -> expresion IGUAL expresion','expresion',3,'p_expresion_binaria','Sintax_.py',127),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_binaria','Sintax_.py',128),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_binaria','Sintax_.py',129),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_binaria','Sintax_.py',130),
  ('expresion -> expresion MENOR_IGUAL expresion','expresion',3,'p_expresion_binaria','Sintax_.py',131),
  ('expresion -> expresion MAYOR_IGUAL expresion','expresion',3,'p_expresion_binaria','Sintax_.py',132),
  ('expresion -> expresion Y expresion','expresion',3,'p_expresion_binaria','Sintax_.py',133),
  ('expresion -> expresion O expresion','expresion',3,'p_expresion_binaria','Sintax_.py',134),
  ('expresion -> NEG expresion','expresion',2,'p_expresion_neg','Sintax_.py',138),
  ('expresion -> PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO','expresion',3,'p_expresion_paren','Sintax_.py',143),
  ('mientras -> MIENTRAS expresion instrucciones FIN MIENTRAS','mientras',5,'p_mientras','Sintax_.py',148),
  ('si -> SI expresion ENTONCES instrucciones sino_opcional','si',5,'p_si','Sintax_.py',156),
  ('sino_opcional -> SINO si','sino_opcional',2,'p_sino_opcional','Sintax_.py',165),
  ('sino_opcional -> SINO instrucciones','sino_opcional',2,'p_sino_opcional','Sintax_.py',166),
  ('sino_opcional -> empty','sino_opcional',1,'p_sino_opcional','Sintax_.py',167),
  ('empty -> <empty>','empty',0,'p_empty','Sintax_.py',175),
]
