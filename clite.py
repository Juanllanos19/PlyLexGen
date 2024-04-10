import ply.lex as lex

tokens = ('FLOAT', 
          'INT',
          'STR')  


states = (
    ('str', 'exclusive'),
)


def t_FLOAT(t):
    r'((((\d(\d|_\d)*)*\.(\d(\d|_\d)*)*)([eE][+-]?(\d(\d|_\d)*)+)?)|((\d(\d|_\d)*)+[eE][+-]?(\d(\d|_\d)*)+))'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+(?:_\d+)*'  
    t.value = int(t.value.replace('_', ''))
    return t

def t_STR(t):
    r'\"'
    t.lexer.str_start = t.lexer.lexpos - 1  # Registra la posición inicial de la cadena
    t.lexer.begin('str')  # Cambia al estado str

def t_error(t):
    raise lex.LexError("Illegal character '%s'" % t.value[0],[])

def t_str_END(t):
    r'\"'
    t.value = t.lexer.lexdata[t.lexer.str_start : t.lexer.lexpos + 1]
    t.type = 'STR'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    return t

def t_str_content(t):
    r'[a-zA-Z\s]+'

def t_str_error(t):
    print("Illegal character '%s' in string" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


def getLexer():
    return lexer
