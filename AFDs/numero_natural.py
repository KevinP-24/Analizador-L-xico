from utils.tokens import TokenType

class AFDNumeroNatural:
    def __init__(self):
        self.estado_inicial = 0
        self.estado_aceptacion = 1

    def reconocer(self, texto, inicio):
        estado = self.estado_inicial
        lexema = ''
        i = inicio

        while i < len(texto):
            caracter = texto[i]

            if caracter.isdigit():
                lexema += caracter
                estado = self.estado_aceptacion
                i += 1
            else:
                break  # Ya no es dígito

        if estado == self.estado_aceptacion and len(lexema) > 0:
            return (lexema, len(lexema), TokenType.NUMERO_NATURAL)
        else:
            return None
