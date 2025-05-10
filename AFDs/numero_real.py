from utils.tokens import TokenType

class AFDNumeroReal:
    def __init__(self):
        self.estado_inicial = 0
        self.estado_aceptacion = 2

    def reconocer(self, texto, inicio):
        estado = self.estado_inicial
        lexema = ''
        i = inicio
        longitud = len(texto)

        while i < longitud:
            c = texto[i]

            if estado == 0:
                if c.isdigit():
                    lexema += c
                    estado = 1
                else:
                    return None
            elif estado == 1:
                if c.isdigit():
                    lexema += c
                elif c == '.':
                    lexema += c
                    estado = 2
                else:
                    return None
            elif estado == 2:
                if c.isdigit():
                    lexema += c
                    estado = 3
                else:
                    return None
            elif estado == 3:
                if c.isdigit():
                    lexema += c
                else:
                    break
            i += 1

        if estado == 3:
            return (lexema, len(lexema), TokenType.NUMERO_REAL)
        else:
            return None
