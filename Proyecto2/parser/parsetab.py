
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftMENORMAYORleftMENORIGMAYORIGleftMASMENOSleftPORDIVIDIDOAND BOOL BREAK CADENA COMA CONSOLE CONTINUE CORDER CORIZQ DECIMAL DIF DIVIDIDO DOSPTS ENTERO FLOAT FUNC ID IF IG IGIG INTERFACE LLAVEDER LLAVEIZQ LOG MAS MAYOR MAYORIG MENOR MENORIG MENOS NOT NUMBER OR PARDER PARIZQ POR PUNTO PYC RETURN STRING TERN VAR WHILEs : blockblock : block instruccion\n            | instruccion instruccion : print\n                | ifinstruction \n                | whileinstruction \n                | declaration\n                | arraydeclaration\n                | assignment\n                | breakstmt\n                | continuestmt\n                | functionstmt\n                | call\n                | returnstmt\n                | interfacecreation\n                | interdeclarationprint : CONSOLE PUNTO LOG PARIZQ expressionList PARDER PYCifinstruction : IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDERwhileinstruction : WHILE PARIZQ expression PARDER LLAVEIZQ block LLAVEDERdeclaration : VAR ID DOSPTS type IG expression PYCarraydeclaration : VAR ID DOSPTS type CORIZQ CORDER IG expression PYCinterdeclaration : VAR ID DOSPTS ID IG LLAVEIZQ interfaceContent LLAVEDER PYCinterfaceContent : interfaceContent COMA ID DOSPTS expression\n                | ID DOSPTS expressionassignment : ID IG expression PYCreturnstmt : RETURN expression PYC\n                | RETURN PYCcall : ID PARIZQ expressionList PARDER PYC\n            | ID PARIZQ PARDER PYCfunctionstmt : FUNC ID funcparams functype LLAVEIZQ block LLAVEDERfuncparams : PARIZQ paramsList PARDER\n                |  PARIZQ PARDERinterfacecreation : INTERFACE ID LLAVEIZQ attributeList LLAVEDER PYCattributeList : attributeList ID DOSPTS type PYC\n                | ID DOSPTS type PYCparamsList : paramsList COMA ID DOSPTS type\n                | ID DOSPTS typefunctype : DOSPTS type\n                | breakstmt : BREAK PYCcontinuestmt : CONTINUE PYCtype : NUMBER\n            | FLOAT\n            | STRING\n            | BOOLexpressionList : expressionList COMA expression\n                    | expression expression : expression MAS expressionexpression : expression MENOS expressionexpression : expression POR expressionexpression : expression DIVIDIDO expressionexpression : expression MAYOR expressionexpression : expression MENOR expressionexpression : expression MAYORIG expressionexpression : expression MENORIG expressionexpression : expression IGIG expressionexpression : expression DIF expressionexpression : expression AND expressionexpression : expression OR expressionexpression : NOT expressionexpression : PARIZQ expression PARDERexpression : expression TERN expression DOSPTS expressionexpression    : ENTERO\n                    | CADENA\n                    | listArrayexpression : CORIZQ expressionList CORDERexpression : ID PARIZQ expressionList PARDER\n            | ID PARIZQ PARDERlistArray : listArray CORIZQ expression CORDER\n                | listArray PUNTO ID\n                | ID'
    
_lr_action_items = {'CONSOLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,118,119,123,125,137,138,142,148,149,150,151,154,156,167,169,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,17,17,-28,17,17,17,17,-33,-17,-18,-19,-20,-30,-22,-21,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,118,119,123,125,137,138,142,148,149,150,151,154,156,167,169,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,18,18,-28,18,18,18,18,-33,-17,-18,-19,-20,-30,-22,-21,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,118,119,123,125,137,138,142,148,149,150,151,154,156,167,169,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,19,19,-28,19,19,19,19,-33,-17,-18,-19,-20,-30,-22,-21,]),'VAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,118,119,123,125,137,138,142,148,149,150,151,154,156,167,169,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,20,20,-28,20,20,20,20,-33,-17,-18,-19,-20,-30,-22,-21,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,24,25,26,27,29,30,32,33,34,35,38,39,40,44,50,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,73,74,76,77,78,87,89,90,116,118,119,121,123,125,128,130,137,138,139,142,148,149,150,151,154,155,156,158,160,162,165,167,169,170,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,31,36,45,46,-2,45,45,45,45,-40,-41,-27,45,45,45,81,95,-26,45,45,45,45,45,45,45,45,45,45,45,45,45,45,111,45,115,45,-25,45,-29,134,21,21,45,-28,21,143,45,21,21,152,21,-33,-17,-18,-19,-20,45,-30,-35,45,168,-34,-22,-21,45,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,118,119,123,125,137,138,142,148,149,150,151,154,156,167,169,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,22,22,-28,22,22,22,22,-33,-17,-18,-19,-20,-30,-22,-21,]),'CONTINUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,118,119,123,125,137,138,142,148,149,150,151,154,156,167,169,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,23,23,-28,23,23,23,23,-33,-17,-18,-19,-20,-30,-22,-21,]),'FUNC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,118,119,123,125,137,138,142,148,149,150,151,154,156,167,169,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,24,24,-28,24,24,24,24,-33,-17,-18,-19,-20,-30,-22,-21,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,118,119,123,125,137,138,142,148,149,150,151,154,156,167,169,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,25,25,-28,25,25,25,25,-33,-17,-18,-19,-20,-30,-22,-21,]),'INTERFACE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,118,119,123,125,137,138,142,148,149,150,151,154,156,167,169,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,26,26,-28,26,26,26,26,-33,-17,-18,-19,-20,-30,-22,-21,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,57,87,90,123,148,149,150,151,154,156,167,169,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-26,-25,-29,-28,-33,-17,-18,-19,-20,-30,-22,-21,]),'LLAVEDER':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,34,35,38,41,42,43,45,57,71,87,90,96,97,98,99,100,101,102,103,104,105,106,107,109,111,112,114,116,123,131,132,137,138,142,145,148,149,150,151,153,154,156,158,165,166,167,169,171,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-40,-41,-27,-63,-64,-65,-71,-26,-60,-25,-29,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-70,-66,-68,135,-28,-69,-67,150,151,156,-62,-33,-17,-18,-19,161,-20,-30,-35,-34,-24,-22,-21,-23,]),'PUNTO':([17,43,45,111,131,],[28,74,-71,-70,-69,]),'PARIZQ':([18,19,21,25,29,30,32,33,36,39,40,44,45,47,58,59,60,61,62,63,64,65,66,67,68,69,70,73,76,78,89,121,130,155,160,170,],[29,30,33,40,40,40,40,40,56,40,40,40,76,78,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'IG':([21,81,82,83,84,85,86,141,],[32,120,121,-42,-43,-44,-45,155,]),'PYC':([22,23,25,37,41,42,43,45,51,53,71,83,84,85,86,88,96,97,98,99,100,101,102,103,104,105,106,107,109,111,112,114,131,132,135,136,140,145,146,159,161,163,],[34,35,38,57,-63,-64,-65,-71,87,90,-60,-42,-43,-44,-45,123,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-70,-66,-68,-69,-67,148,149,154,-62,158,165,167,169,]),'NOT':([25,29,30,32,33,39,40,44,58,59,60,61,62,63,64,65,66,67,68,69,70,73,76,78,89,121,130,155,160,170,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'ENTERO':([25,29,30,32,33,39,40,44,58,59,60,61,62,63,64,65,66,67,68,69,70,73,76,78,89,121,130,155,160,170,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'CADENA':([25,29,30,32,33,39,40,44,58,59,60,61,62,63,64,65,66,67,68,69,70,73,76,78,89,121,130,155,160,170,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'CORIZQ':([25,29,30,32,33,39,40,43,44,45,58,59,60,61,62,63,64,65,66,67,68,69,70,73,76,78,82,83,84,85,86,89,111,121,130,131,155,160,170,],[44,44,44,44,44,44,44,73,44,-71,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,122,-42,-43,-44,-45,44,-70,44,44,-69,44,44,44,]),'LOG':([28,],[47,]),'DOSPTS':([31,41,42,43,45,55,71,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,114,115,127,131,132,134,143,145,152,168,],[50,-63,-64,-65,-71,92,-60,-32,129,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,130,-61,-70,-66,-68,133,-31,-69,-67,147,157,-62,160,170,]),'PARDER':([33,41,42,43,45,48,49,52,54,56,71,72,76,83,84,85,86,93,96,97,98,99,100,101,102,103,104,105,106,107,109,111,112,113,114,117,124,131,132,144,145,164,],[53,-63,-64,-65,-71,79,80,88,-47,94,-60,109,114,-42,-43,-44,-45,127,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-70,-66,132,-68,136,-46,-69,-67,-37,-62,-36,]),'MAS':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[58,-63,-64,-65,-71,58,58,58,58,58,58,-48,-49,-50,-51,58,58,58,58,58,58,58,58,58,-61,58,-70,-66,-68,58,-69,-67,58,58,58,58,58,]),'MENOS':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[59,-63,-64,-65,-71,59,59,59,59,59,59,-48,-49,-50,-51,59,59,59,59,59,59,59,59,59,-61,59,-70,-66,-68,59,-69,-67,59,59,59,59,59,]),'POR':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[60,-63,-64,-65,-71,60,60,60,60,60,60,60,60,-50,-51,60,60,60,60,60,60,60,60,60,-61,60,-70,-66,-68,60,-69,-67,60,60,60,60,60,]),'DIVIDIDO':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[61,-63,-64,-65,-71,61,61,61,61,61,61,61,61,-50,-51,61,61,61,61,61,61,61,61,61,-61,61,-70,-66,-68,61,-69,-67,61,61,61,61,61,]),'MAYOR':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[62,-63,-64,-65,-71,62,62,62,62,62,62,-48,-49,-50,-51,-52,-53,-54,-55,62,62,62,62,62,-61,62,-70,-66,-68,62,-69,-67,62,62,62,62,62,]),'MENOR':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[63,-63,-64,-65,-71,63,63,63,63,63,63,-48,-49,-50,-51,-52,-53,-54,-55,63,63,63,63,63,-61,63,-70,-66,-68,63,-69,-67,63,63,63,63,63,]),'MAYORIG':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[64,-63,-64,-65,-71,64,64,64,64,64,64,-48,-49,-50,-51,64,64,-54,-55,64,64,64,64,64,-61,64,-70,-66,-68,64,-69,-67,64,64,64,64,64,]),'MENORIG':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[65,-63,-64,-65,-71,65,65,65,65,65,65,-48,-49,-50,-51,65,65,-54,-55,65,65,65,65,65,-61,65,-70,-66,-68,65,-69,-67,65,65,65,65,65,]),'IGIG':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[66,-63,-64,-65,-71,66,66,66,66,66,66,-48,-49,-50,-51,-52,-53,-54,-55,66,66,-58,-59,66,-61,66,-70,-66,-68,66,-69,-67,66,66,66,66,66,]),'DIF':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[67,-63,-64,-65,-71,67,67,67,67,67,67,-48,-49,-50,-51,-52,-53,-54,-55,67,67,-58,-59,67,-61,67,-70,-66,-68,67,-69,-67,67,67,67,67,67,]),'AND':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[68,-63,-64,-65,-71,68,68,68,68,68,68,-48,-49,-50,-51,-52,-53,-54,-55,68,68,-58,68,68,-61,68,-70,-66,-68,68,-69,-67,68,68,68,68,68,]),'OR':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[69,-63,-64,-65,-71,69,69,69,69,69,69,-48,-49,-50,-51,-52,-53,-54,-55,69,69,-58,-59,69,-61,69,-70,-66,-68,69,-69,-67,69,69,69,69,69,]),'TERN':([37,41,42,43,45,48,49,51,54,71,72,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,124,131,132,140,145,163,166,171,],[70,-63,-64,-65,-71,70,70,70,70,70,70,-48,-49,-50,-51,-52,-53,-54,-55,70,70,-58,-59,70,-61,70,-70,-66,-68,70,-69,-67,70,70,70,70,70,]),'COMA':([41,42,43,45,52,54,71,75,83,84,85,86,93,96,97,98,99,100,101,102,103,104,105,106,107,109,111,112,113,114,117,124,131,132,144,145,153,164,166,171,],[-63,-64,-65,-71,89,-47,-60,89,-42,-43,-44,-45,128,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-70,-66,89,-68,89,-46,-69,-67,-37,-62,162,-36,-24,-23,]),'CORDER':([41,42,43,45,54,71,75,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,122,124,131,132,145,],[-63,-64,-65,-71,-47,-60,112,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,131,-70,-66,-68,141,-46,-69,-67,-62,]),'LLAVEIZQ':([46,55,79,80,83,84,85,86,91,94,120,126,127,],[77,-39,118,119,-42,-43,-44,-45,125,-32,139,-38,-31,]),'NUMBER':([50,92,129,133,147,157,],[83,83,83,83,83,83,]),'FLOAT':([50,92,129,133,147,157,],[84,84,84,84,84,84,]),'STRING':([50,92,129,133,147,157,],[85,85,85,85,85,85,]),'BOOL':([50,92,129,133,147,157,],[86,86,86,86,86,86,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'s':([0,],[1,]),'block':([0,118,119,125,],[2,137,138,142,]),'instruccion':([0,2,118,119,125,137,138,142,],[3,27,3,3,3,27,27,27,]),'print':([0,2,118,119,125,137,138,142,],[4,4,4,4,4,4,4,4,]),'ifinstruction':([0,2,118,119,125,137,138,142,],[5,5,5,5,5,5,5,5,]),'whileinstruction':([0,2,118,119,125,137,138,142,],[6,6,6,6,6,6,6,6,]),'declaration':([0,2,118,119,125,137,138,142,],[7,7,7,7,7,7,7,7,]),'arraydeclaration':([0,2,118,119,125,137,138,142,],[8,8,8,8,8,8,8,8,]),'assignment':([0,2,118,119,125,137,138,142,],[9,9,9,9,9,9,9,9,]),'breakstmt':([0,2,118,119,125,137,138,142,],[10,10,10,10,10,10,10,10,]),'continuestmt':([0,2,118,119,125,137,138,142,],[11,11,11,11,11,11,11,11,]),'functionstmt':([0,2,118,119,125,137,138,142,],[12,12,12,12,12,12,12,12,]),'call':([0,2,118,119,125,137,138,142,],[13,13,13,13,13,13,13,13,]),'returnstmt':([0,2,118,119,125,137,138,142,],[14,14,14,14,14,14,14,14,]),'interfacecreation':([0,2,118,119,125,137,138,142,],[15,15,15,15,15,15,15,15,]),'interdeclaration':([0,2,118,119,125,137,138,142,],[16,16,16,16,16,16,16,16,]),'expression':([25,29,30,32,33,39,40,44,58,59,60,61,62,63,64,65,66,67,68,69,70,73,76,78,89,121,130,155,160,170,],[37,48,49,51,54,71,72,54,96,97,98,99,100,101,102,103,104,105,106,107,108,110,54,54,124,140,145,163,166,171,]),'listArray':([25,29,30,32,33,39,40,44,58,59,60,61,62,63,64,65,66,67,68,69,70,73,76,78,89,121,130,155,160,170,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'expressionList':([33,44,76,78,],[52,75,113,117,]),'funcparams':([36,],[55,]),'type':([50,92,129,133,147,157,],[82,126,144,146,159,164,]),'functype':([55,],[91,]),'paramsList':([56,],[93,]),'attributeList':([77,],[116,]),'interfaceContent':([139,],[153,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> s","S'",1,None,None,None),
  ('s -> block','s',1,'p_start','parser.py',182),
  ('block -> block instruccion','block',2,'p_instruction_block','parser.py',186),
  ('block -> instruccion','block',1,'p_instruction_block','parser.py',187),
  ('instruccion -> print','instruccion',1,'p_instruction_list','parser.py',196),
  ('instruccion -> ifinstruction','instruccion',1,'p_instruction_list','parser.py',197),
  ('instruccion -> whileinstruction','instruccion',1,'p_instruction_list','parser.py',198),
  ('instruccion -> declaration','instruccion',1,'p_instruction_list','parser.py',199),
  ('instruccion -> arraydeclaration','instruccion',1,'p_instruction_list','parser.py',200),
  ('instruccion -> assignment','instruccion',1,'p_instruction_list','parser.py',201),
  ('instruccion -> breakstmt','instruccion',1,'p_instruction_list','parser.py',202),
  ('instruccion -> continuestmt','instruccion',1,'p_instruction_list','parser.py',203),
  ('instruccion -> functionstmt','instruccion',1,'p_instruction_list','parser.py',204),
  ('instruccion -> call','instruccion',1,'p_instruction_list','parser.py',205),
  ('instruccion -> returnstmt','instruccion',1,'p_instruction_list','parser.py',206),
  ('instruccion -> interfacecreation','instruccion',1,'p_instruction_list','parser.py',207),
  ('instruccion -> interdeclaration','instruccion',1,'p_instruction_list','parser.py',208),
  ('print -> CONSOLE PUNTO LOG PARIZQ expressionList PARDER PYC','print',7,'p_instruction_console','parser.py',212),
  ('ifinstruction -> IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER','ifinstruction',7,'p_instruction_if','parser.py',217),
  ('whileinstruction -> WHILE PARIZQ expression PARDER LLAVEIZQ block LLAVEDER','whileinstruction',7,'p_instruction_while','parser.py',222),
  ('declaration -> VAR ID DOSPTS type IG expression PYC','declaration',7,'p_instruction_declaration','parser.py',227),
  ('arraydeclaration -> VAR ID DOSPTS type CORIZQ CORDER IG expression PYC','arraydeclaration',9,'p_instruction_array_declaration','parser.py',232),
  ('interdeclaration -> VAR ID DOSPTS ID IG LLAVEIZQ interfaceContent LLAVEDER PYC','interdeclaration',9,'p_instruction_interface_declaration','parser.py',237),
  ('interfaceContent -> interfaceContent COMA ID DOSPTS expression','interfaceContent',5,'p_instruction_interface_content','parser.py',242),
  ('interfaceContent -> ID DOSPTS expression','interfaceContent',3,'p_instruction_interface_content','parser.py',243),
  ('assignment -> ID IG expression PYC','assignment',4,'p_instruction_assignment','parser.py',254),
  ('returnstmt -> RETURN expression PYC','returnstmt',3,'p_instruction_return','parser.py',259),
  ('returnstmt -> RETURN PYC','returnstmt',2,'p_instruction_return','parser.py',260),
  ('call -> ID PARIZQ expressionList PARDER PYC','call',5,'p_instruction_call_function','parser.py',268),
  ('call -> ID PARIZQ PARDER PYC','call',4,'p_instruction_call_function','parser.py',269),
  ('functionstmt -> FUNC ID funcparams functype LLAVEIZQ block LLAVEDER','functionstmt',7,'p_instruction_function','parser.py',277),
  ('funcparams -> PARIZQ paramsList PARDER','funcparams',3,'p_instruction_function_params_list','parser.py',282),
  ('funcparams -> PARIZQ PARDER','funcparams',2,'p_instruction_function_params_list','parser.py',283),
  ('interfacecreation -> INTERFACE ID LLAVEIZQ attributeList LLAVEDER PYC','interfacecreation',6,'p_instruction_interface_creation','parser.py',290),
  ('attributeList -> attributeList ID DOSPTS type PYC','attributeList',5,'p_instruction_interface_attribute','parser.py',295),
  ('attributeList -> ID DOSPTS type PYC','attributeList',4,'p_instruction_interface_attribute','parser.py',296),
  ('paramsList -> paramsList COMA ID DOSPTS type','paramsList',5,'p_expression_param_list','parser.py',307),
  ('paramsList -> ID DOSPTS type','paramsList',3,'p_expression_param_list','parser.py',308),
  ('functype -> DOSPTS type','functype',2,'p_instruction_function_type','parser.py',319),
  ('functype -> <empty>','functype',0,'p_instruction_function_type','parser.py',320),
  ('breakstmt -> BREAK PYC','breakstmt',2,'p_instruction_break','parser.py',327),
  ('continuestmt -> CONTINUE PYC','continuestmt',2,'p_instruction_continue','parser.py',332),
  ('type -> NUMBER','type',1,'p_type_prod','parser.py',337),
  ('type -> FLOAT','type',1,'p_type_prod','parser.py',338),
  ('type -> STRING','type',1,'p_type_prod','parser.py',339),
  ('type -> BOOL','type',1,'p_type_prod','parser.py',340),
  ('expressionList -> expressionList COMA expression','expressionList',3,'p_expression_list','parser.py',351),
  ('expressionList -> expression','expressionList',1,'p_expression_list','parser.py',352),
  ('expression -> expression MAS expression','expression',3,'p_expression_add','parser.py',362),
  ('expression -> expression MENOS expression','expression',3,'p_expression_sub','parser.py',367),
  ('expression -> expression POR expression','expression',3,'p_expression_mult','parser.py',372),
  ('expression -> expression DIVIDIDO expression','expression',3,'p_expression_div','parser.py',377),
  ('expression -> expression MAYOR expression','expression',3,'p_expression_mayor','parser.py',382),
  ('expression -> expression MENOR expression','expression',3,'p_expression_menor','parser.py',387),
  ('expression -> expression MAYORIG expression','expression',3,'p_expression_mayor_igual','parser.py',392),
  ('expression -> expression MENORIG expression','expression',3,'p_expression_menor_igual','parser.py',397),
  ('expression -> expression IGIG expression','expression',3,'p_expression_igual','parser.py',402),
  ('expression -> expression DIF expression','expression',3,'p_expression_diferente','parser.py',407),
  ('expression -> expression AND expression','expression',3,'p_expression_and','parser.py',412),
  ('expression -> expression OR expression','expression',3,'p_expression_or','parser.py',417),
  ('expression -> NOT expression','expression',2,'p_expression_not','parser.py',422),
  ('expression -> PARIZQ expression PARDER','expression',3,'p_expression_agrupacion','parser.py',427),
  ('expression -> expression TERN expression DOSPTS expression','expression',5,'p_expression_ternario','parser.py',431),
  ('expression -> ENTERO','expression',1,'p_expression_primitiva','parser.py',436),
  ('expression -> CADENA','expression',1,'p_expression_primitiva','parser.py',437),
  ('expression -> listArray','expression',1,'p_expression_primitiva','parser.py',438),
  ('expression -> CORIZQ expressionList CORDER','expression',3,'p_expression_array_primitiva','parser.py',442),
  ('expression -> ID PARIZQ expressionList PARDER','expression',4,'p_expression_call_function','parser.py',447),
  ('expression -> ID PARIZQ PARDER','expression',3,'p_expression_call_function','parser.py',448),
  ('listArray -> listArray CORIZQ expression CORDER','listArray',4,'p_expression_list_array','parser.py',456),
  ('listArray -> listArray PUNTO ID','listArray',3,'p_expression_list_array','parser.py',457),
  ('listArray -> ID','listArray',1,'p_expression_list_array','parser.py',458),
]