from errores import ErrorLexico
from utils.tokens import TokenType

from AFDs.afd_identificador import AFDIdentificador
from AFDs.numero_real import AFDNumeroReal
from AFDs.numero_natural import AFDNumeroNatural
from AFDs.operador import AFDOperador

class Lexer:
    def __init__(self):
        # Orden importa: primero número real, luego natural, para evitar conflictos como "3.14"
        self.afds = [
            AFDIdentificador(),   # Identificadores (nombres de variables, etc.)
            AFDNumeroReal(),      # Números reales (ej: 3.14)
            AFDNumeroNatural(),   # Números naturales (ej: 42)
            AFDOperador(),        # Todos los operadores clasificados por tipo
        ]

    def analizar(self, texto):
        tokens = []
        linea = 1
        columna = 1
        i = 0
        longitud = len(texto)

        while i < longitud:
            # Ignorar espacios y saltos de línea
            if texto[i].isspace():
                if texto[i] == '\n':
                    linea += 1
                    columna = 1
                else:
                    columna += 1
                i += 1
                continue
            reconocio = False
            for afd in self.afds:
                resultado = afd.reconocer(texto, i)
                if resultado:
                    lexema, longitud_token, categoria = resultado
                    tokens.append({
                        'lexema': lexema,
                        'categoria': categoria,
                        'linea': linea,
                        'columna': columna
                    })
                    i += longitud_token
                    columna += longitud_token
                    reconocio = True
                    break

            if not reconocio:
                raise ErrorLexico(f"Token no reconocido: {texto[i]}", linea, columna)

        return tokens
