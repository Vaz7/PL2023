import ply.lex as lex

# Lista de nomes dos tokens
tokens = [
    'ID',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
    'EQUALS',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LT',
    'GT',
    'NUMBER',
    'RANGE',
]

# Palavras reservadas
reserved = {
    'int': 'INT',
    'function': 'FUNCTION',
    'program': 'PROGRAM',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'if': 'IF',
    'print': 'PRINT',
}

tokens += list(reserved.values())

# Expressões regulares para os tokens simples
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_RANGE = r'\.\.'


# Expressões regulares para tokens mais complexos
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Comentários
def t_COMMENT(t):
    r'(//.*|/\*[\s\S]*?\*/|--.*)'
    pass

# Nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Erro
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Função de teste
def test_lexer(input_str):
    lexer.input(input_str)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

if __name__ == "__main__":
    # Teste os exemplos
    exemplo1 = '''/* factorial.p
    -- 2023-03-20
    -- by jcr
    */
    int i;
    // Função que calcula o factorial dum número n
    function fact(n){
      int res = 1;
      while res > 1 {
        res = res * n;
        res = res - 1;
      }
    }
    // Programa principal
    program myFact{
      for i in [1..10]{
        print(i, fact(i));
      }
    }'''

    exemplo2 = '''/* max.p: calcula o maior inteiro duma lista desordenada
    -- 2023-03-20
    -- by jcr
    */
    int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};
    // Programa principal
    program myMax{
      int max = a[0];
      for i in [1..9]{
        if max < a[i] {
          max = a[i];
        }
      }
      print(max);
    }'''

    # Teste os exemplos
    tokens1 = test_lexer(exemplo1)
    for token in tokens1:
        print(token)

    print("\nExemplo 2:\n")
    tokens2 = test_lexer(exemplo2)
    for token in tokens2:
        print(token)