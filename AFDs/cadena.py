from utils.tokens import TokenType

class AFDCadenaCaracteres:
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
                if c == '"':
                    lexema += c
                    estado = 1
                else:
                    return None
            elif estado == 1:
                if c == '\\':  # carácter de escape
                    if i + 1 < longitud:
                        lexema += c + texto[i + 1]
                        i += 1
                    else:
                        # cadena termina abruptamente con \
                        return None
                elif c == '"':
                    lexema += c
                    estado = 2
                    i += 1
                    break
                else:
                    lexema += c
            i += 1

        if estado == 2:
            return (lexema, len(lexema), TokenType.CADENA)
        else:
            # Error: cadena sin cerrar
            return ('"' + lexema, len(lexema)+1, TokenType.ERROR)
