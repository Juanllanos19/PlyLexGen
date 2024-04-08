import ply.lex as lex

tokens = ['FLOAT', 'INT']  

t_ignore = ' \t'


def t_FLOAT(t):
    r'\d+(\.\d*)?(e[-+]?\d+)?|\.\d+(e[-+]?\d+)?'  
    t.value = float(t.value)
    return t



def t_INT(t):
    r'\d+(?:_\d+)*'  
    t.value = int(t.value.replace('_', ''))
    return t


lexer = lex.lex()


def getLexer():
    return lexer
