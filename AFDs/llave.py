from utils.tokens import TokenType

class AFDLlave:
    def __init__(self):
        self.estado_inicial = 0
        self.estado_aceptacion = 1

    def reconocer(self, texto, inicio):
        if inicio < len(texto):
            c = texto[inicio]
            if c == '{' or c == '}':
                return (c, 1, TokenType.LLAVE)
        return None
