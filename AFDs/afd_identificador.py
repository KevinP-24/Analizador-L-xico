from utils.tokens import TokenType

class AFDIdentificador:
    def __init__(self):
        self.estado_inicial = 0
        self.estado_aceptacion = 1

    def reconocer(self, texto, inicio):
        estado = self.estado_inicial
        lexema = ''
        i = inicio
        max_longitud = 10

        while i < len(texto) and len(lexema) < max_longitud:
            caracter = texto[i]

            if estado == 0:
                if caracter.isalpha() or caracter == '_':
                    lexema += caracter
                    estado = 1
                else:
                    return None  # No cumple condición de inicio
            elif estado == 1:
                if caracter.isalnum() or caracter == '_':
                    lexema += caracter
                else:
                    break  # Finaliza el lexema
            i += 1

        # Si terminó en estado de aceptación y el lexema tiene al menos 1 carácter
        if estado == self.estado_aceptacion and len(lexema) > 0:
            return (lexema, len(lexema), TokenType.IDENTIFICADOR)
        else:
            return None
