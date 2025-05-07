from lexer import Lexer

entrada = "edad = 25 + 5 == 30 && true"


lexer = Lexer()
tokens = lexer.analizar(entrada)

print("--- Tokens reconocidos ---")
for token in tokens:
    print(f"{token['categoria'].value} - '{token['lexema']}' en línea {token['linea']}, columna {token['columna']}")
