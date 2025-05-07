from errores import ErrorLexico
from AFDs.afd_identificador import AFDIdentificador
from AFDs.numero_natural import AFDNumeroNatural
from AFDs.operador import AFDOperador
from utils.tokens import TokenType

class Lexer:
    def __init__(self):
        # Lista de AFDs a ejecutar en orden
        self.afds = [
            AFDIdentificador(), #Para cadaenas
            AFDNumeroNatural(), #Para numeros naturales
            AFDOperador(),      #Para operadores logicos
        ]
    
    def analizar(self, texto):
        tokens = []
        linea = 1
        columna = 1
        i = 0
        longitud = len(texto)

        while i < longitud:
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
