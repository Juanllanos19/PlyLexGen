import ply.lex as lex

tokens = ('FLOAT', 
          'INT')  

t_ignore = ' \t'


def t_FLOAT(t):
    r'((((\d(\d|_\d)*)*\.(\d(\d|_\d)*)*)([eE][+-]?(\d(\d|_\d)*)+)?)|((\d(\d|_\d)*)+[eE][+-]?(\d(\d|_\d)*)+))'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+(?:_\d+)*'  
    t.value = int(t.value.replace('_', ''))
    return t

def t_error(t):
    raise lex.LexError("Illegal character '%s'" % t.value[0],[])

lexer = lex.lex()


def getLexer():
    return lexer
