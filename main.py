# -----------------------------------
# ANALIZADOR LEXICO.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape,
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea)

#palabras resevadas
reserved = {
    'int': 'TYPE_INT',
    'bool': 'TYPE_BOOL',
    'float': 'TYPE_FLOAT',
    'string': 'TYPE_STRING',
    'char': 'TYPE_CHAR',
    'double': 'TYPE_DOUBLE',
    'long': 'TYPE_LONG',
    'cin': 'INPUT',
    'cout': 'OUPUT',
    'return': 'RETURN_VALUE',
    'if':  'TYPE_STRUCT_IF',
    'else': 'TYPE_STRUCT_ELSE',
    'while': 'TYPE_STRUCT_WHILE',
    'do':'TYPE_STRUCT_DO',
    'for': 'TYPE_STRUCT_FOR'
  
}

#  tokens 
tokens = [
    'NUM','DEC', 'SUM', 'SUBSTRACTION', 'MULTIPLICATION', 'DIVIDE', 'MODULE',
    'PARENT_LEFT', 'PARENT_RIGHT', 'DOTCOM', 'DOT', 'COMMA', 'OPER_MAYOR',
    'OPER_MENOR', 'K_LEFT', 'K_RIGHT', 'OPER_O', 'OPER_Y', 'OPER_NO', 'ID','EQUAL',
'2DOTS','INCREMENT','DECREMENT','OPER_MAYOR_EQ',
  'OPER_MENOR_EQ','DIFERENT', 'DEZ_IZQ','DEZ_DER','COMILLA','COMENT','COMENT_DER',
  'COMENT_IZQ', 'SUB_G', 'COMENT_MULTI'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_SUM = r'\+'
t_SUBSTRACTION = r'-'
t_MULTIPLICATION = r'\*'
t_DIVIDE = r'/'
t_MODULE = r'\%'
t_PARENT_LEFT = r'\('
t_PARENT_RIGHT = r'\)'
t_DOTCOM = r';'
t_DOT = r'\.'
t_COMMA = r','
t_OPER_MAYOR = r'>'
t_OPER_MENOR = r'<'
t_K_LEFT = r'\{'
t_K_RIGHT = r'\}'
t_EQUAL = r'='
t_OPER_Y = r'\&&'
t_2DOTS = r'\:'
t_INCREMENT = r'\++'
t_DECREMENT = r'\--'
t_OPER_MAYOR_EQ = r'\>='
t_OPER_MENOR_EQ = r'\<='
t_DIFERENT = r'!='
t_DEZ_IZQ = r'\<<'
t_DEZ_DER = r'\>>'
t_COMILLA = r'\"'
#t_COMENT = r'\//'
t_COMENT = r'\/\/.*'


t_COMENT_DER = r'\ /*'
t_COMENT_IZQ = r'\*/'
t_SUB_G = r'\_'


#t_OPER_O = r'\||'
#t_OPER_NOT = r'\!'

#t_NUMBER  = r'\d+'

#COMENTARIO MULTIPLE

def t_COMENT_MULTI(t):
    r'\/\*[^*]*\*+([^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')

#identificadores
def t_ID(t):
  r'[a-zA-Z_]+ ( [a-zA-Z0-9_]* )'
  t.type = reserved.get(t.value, 'ID')  # Check for reserved words
  return t

# A regular expression rule with some action code
def t_NUM(t):
  r'\d+'
  t.value = int(t.value)  # guardamos el valor del lexema
  #print("se reconocio el numero")
  return t


def t_DEC(t):
    r'\d+(\.\d+)?|\.\d+'
    t.value = float(t.value)  # Convertir el valor a float
    return t



# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\n'


# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

##AGREGADO
# Build the lexer
lexer = lex.lex()

# Function to tokenize a given file
def tokenize_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        lexer.input(data)
        tokens = []
        for tok in lexer:
            tokens.append({'TYPE': tok.type, 'VALUE': tok.value, 'LINENO': tok.lineno,'LEXPOS': tok.lexpos})
        return tokens

# Tokenize and print tokens for each file
files = ["hola_mundo.txt", "estructuras_control.txt", "uso_funciones.txt"]
for file_name in files:
    print("\n\t",f"Tokens in {file_name}:")
    tokens = tokenize_file(file_name)
    for token in tokens:
        print(token)