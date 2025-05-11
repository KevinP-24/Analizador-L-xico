from utils.tokens import TokenType

class AFDIncremento:
    def __init__(self):
        self.operadores = {"++", "--"}

    def reconocer(self, texto, inicio):
        if inicio + 1 < len(texto):
            par = texto[inicio:inicio+2]
            if par in self.operadores:
                return (par, 2, TokenType.OPERADOR_INCREMENTO)
        return None
