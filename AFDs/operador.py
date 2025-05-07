from utils.tokens import TokenType

class AFDOperador:
    def __init__(self):
        self.operadores = {
            "=", "+", "-", "*", "/", "%", "==", "!=", "<", ">", "<=", ">=", "&&", "||", "!", "++", "--"
        }

    def reconocer(self, texto, inicio):
        # Intentamos reconocer operadores de 2 caracteres primero
        candidatos = [texto[inicio:inicio+2], texto[inicio]]

        for lexema in candidatos:
            if lexema in self.operadores:
                return (lexema, len(lexema), TokenType.OPERADOR)

        return None
