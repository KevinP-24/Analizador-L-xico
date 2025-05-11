from utils.tokens import TokenType

class AFDPalabraReservada:
    def __init__(self):
        self.estado_inicial = 0
        self.estados_aceptacion = {
            "if": 2,
            "else": 6,
            "while": 11,
            "def": 14,
            "return": 20,
            "class": 25
        }

    def reconocer(self, texto, inicio):
        i = inicio
        estado = self.estado_inicial
        lexema = ''
        longitud = len(texto)

        while i < longitud:
            c = texto[i]

            if estado == 0:
                if c == 'i':
                    estado = 1
                elif c == 'e':
                    estado = 3
                elif c == 'w':
                    estado = 7
                elif c == 'd':
                    estado = 12
                elif c == 'r':
                    estado = 15
                elif c == 'c':
                    estado = 21
                else:
                    return None
                lexema += c

            # "if"
            elif estado == 1 and c == 'f':
                lexema += c
                estado = 2
                i += 1
                break

            # "else"
            elif estado == 3 and c == 'l':
                lexema += c
                estado = 4
            elif estado == 4 and c == 's':
                lexema += c
                estado = 5
            elif estado == 5 and c == 'e':
                lexema += c
                estado = 6
                i += 1
                break

            # "while"
            elif estado == 7 and c == 'h':
                lexema += c
                estado = 8
            elif estado == 8 and c == 'i':
                lexema += c
                estado = 9
            elif estado == 9 and c == 'l':
                lexema += c
                estado = 10
            elif estado == 10 and c == 'e':
                lexema += c
                estado = 11
                i += 1
                break

            # "def"
            elif estado == 12 and c == 'e':
                lexema += c
                estado = 13
            elif estado == 13 and c == 'f':
                lexema += c
                estado = 14
                i += 1
                break

            # "return"
            elif estado == 15 and c == 'e':
                lexema += c
                estado = 16
            elif estado == 16 and c == 't':
                lexema += c
                estado = 17
            elif estado == 17 and c == 'u':
                lexema += c
                estado = 18
            elif estado == 18 and c == 'r':
                lexema += c
                estado = 19
            elif estado == 19 and c == 'n':
                lexema += c
                estado = 20
                i += 1
                break

            # "class"
            elif estado == 21 and c == 'l':
                lexema += c
                estado = 22
            elif estado == 22 and c == 'a':
                lexema += c
                estado = 23
            elif estado == 23 and c == 's':
                lexema += c
                estado = 24
            elif estado == 24 and c == 's':
                lexema += c
                estado = 25
                i += 1
                break

            else:
                return None

            i += 1

        # Confirmar si el estado es de aceptación
        if estado in self.estados_aceptacion.values():
            return (lexema, len(lexema), TokenType.PALABRA_RESERVADA)
        else:
            return None
