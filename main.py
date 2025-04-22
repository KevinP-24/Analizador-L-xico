from lexer import analizar

codigo = 'if x == 10 { return x + 1; }'
resultado = analizar(codigo)

for tipo, valor in resultado:
    print(f"{tipo}: {valor}")
