import ply.lex as lex

tokens = [ 'INT' ]

t_ignore  = ' \t'

def t_INT(t):
    r'\d+(?:_\d+)*' 
    t.value = int(t.value.replace('_', ''))
    return t

lexer = lex.lex()

def getLexer():
    return lexer