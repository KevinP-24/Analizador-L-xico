from utils.tokens import TokenType

class AFDLogico:
    def __init__(self):
        self.operadores = {"&&", "||", "!"}

    def reconocer(self, texto, inicio):
        candidatos = [texto[inicio:inicio+2], texto[inicio:inicio+1]]
        for op in candidatos:
            if op in self.operadores:
                return (op, len(op), TokenType.OPERADOR_LOGICO)
        return None
