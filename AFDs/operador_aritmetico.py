from utils.tokens import TokenType

class AFDAritmetico:
    def __init__(self):
        self.operadores = {"+", "-", "*", "/", "%"}

    def reconocer(self, texto, inicio):
        if inicio < len(texto):
            c = texto[inicio]
            if c in self.operadores:
                return (c, 1, TokenType.OPERADOR_ARITMETICO)
        return None
