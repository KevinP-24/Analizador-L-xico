from lexer import Lexer

entrada = "precio = 3.14 + 2"

lexer = Lexer()
tokens = lexer.analizar(entrada)

for token in tokens:
    print(f"{token['categoria'].value} - '{token['lexema']}' en línea {token['linea']}, columna {token['columna']}")
