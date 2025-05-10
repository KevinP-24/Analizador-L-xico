from utils.tokens import TokenType

class AFDOperador:
    def __init__(self):
        self.grupos_operadores = {
            TokenType.OPERADOR_ASIGNACION: {"="},
            TokenType.OPERADOR_ARITMETICO: {"+", "-", "*", "/", "%"},
            TokenType.OPERADOR_COMPARACION: {"==", "!=", "<", ">", "<=", ">="},
            TokenType.OPERADOR_LOGICO: {"&&", "||", "!"},
            TokenType.OPERADOR_INCREMENTO: {"++", "--"},
        }

    def reconocer(self, texto, inicio):
        # Probar primero con 2 caracteres, luego con 1
        candidatos = [texto[inicio:inicio+2], texto[inicio]]

        for lexema in candidatos:
            for categoria, conjunto in self.grupos_operadores.items():
                if lexema in conjunto:
                    return (lexema, len(lexema), categoria)

        return None
