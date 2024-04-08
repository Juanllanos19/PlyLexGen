import ply.lex as lex

tokens = [ 'INT' ]

t_ignore  = ' \t'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

lexer = lex.lex()

def getLexer():
    return lexer