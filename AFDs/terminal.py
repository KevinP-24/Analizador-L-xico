from utils.tokens import TokenType

class AFDTerminal:
    def __init__(self):
        self.estado_inicial = 0
        self.estado_aceptacion = 1

    def reconocer(self, texto, inicio):
        if inicio < len(texto) and texto[inicio] == ';':
            return (';', 1, TokenType.TERMINAL)
        return None
