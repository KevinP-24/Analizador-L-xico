from utils.tokens import TokenType

class AFDAtribucion:
    def __init__(self):
        self.operador = "="

    def reconocer(self, texto, inicio):
        if inicio < len(texto) and texto[inicio] == self.operador:
            # Evitar confusión con "=="
            if inicio + 1 < len(texto) and texto[inicio + 1] == '=':
                return None
            return ('=', 1, TokenType.OPERADOR_ASIGNACION)
        return None
