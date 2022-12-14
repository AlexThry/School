from ply import lex
from ply import yacc


###################################################
## LEXER
###################################################

reserved = {
    'get' : 'GET',
    'and' : 'AND',
    'or' : 'OR',
    'contains' : 'CONTAINS',
    'exclude' : 'EXCLUDE',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'diff' : 'DIFF'
}

tokens = ['URL', 'NAME'] + list(reserved.values())

t_ignore= ' \t\n'

def t_URL(t):
    r'(https://|http://)[A-Za-z0-9\./\?_]+'
    t.type = reserved.get(t.value, 'URL')
    return t
    
def t_NAME(t):
    r'[A-Za-z0-9][A-Za-z0-9]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_error(t):
    print("error")
    
lex.lex()


###################################################
## PARSER
###################################################

def p_expression(p):
    '''expression : GET URL
    | GET URL instruction'''
    
def p_instruction(p):
    '''instruction : contrainte UNION contrainte
    | instruction INTERSECT contrainte
    | instruction DIFF contrainte
    | instruction OR contrainte
    | instruction AND contrainte
    | contrainte'''
    
def p_contrainte(p):
    '''contrainte : CONTAINS NAME
    | EXCLUDE NAME'''
    
def p_error(p):
    print("error")
    
    
yacc.yacc()
yacc.parse("get http://oui/non.pourquoi contains blabla and exclude baba and exclude chacha")


while True:
    i = input("Idule 1.0 >>> ")
    if i == "quit()":
        break
    lex.input(i)
    while True:
        tok = lex.token() #lecture du prochain token ou none
        if not tok: break
        print(tok)