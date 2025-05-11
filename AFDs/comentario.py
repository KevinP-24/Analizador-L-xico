from utils.tokens import TokenType

class AFDComentario:
    def __init__(self):
        self.estado_inicial = 0

    def reconocer(self, texto, inicio):
        i = inicio
        longitud = len(texto)
        lexema = ''

        if i + 1 >= longitud:
            return None

        # Comentario de línea
        if texto[i] == '/' and texto[i + 1] == '/':
            lexema += '//'
            i += 2
            while i < longitud and texto[i] != '\n':
                lexema += texto[i]
                i += 1
            return (lexema, len(lexema), TokenType.COMENTARIO)

        # Comentario de bloque
        if texto[i] == '/' and texto[i + 1] == '*':
            lexema += '/*'
            i += 2
            cerrado = False
            while i < longitud:
                if texto[i] == '*' and i + 1 < longitud and texto[i + 1] == '/':
                    lexema += '*/'
                    i += 2
                    cerrado = True
                    break
                lexema += texto[i]
                i += 1
            if cerrado:
                return (lexema, len(lexema), TokenType.COMENTARIO)
            else:
                return (lexema, len(lexema), TokenType.ERROR)  # sin cerrar

        return None
