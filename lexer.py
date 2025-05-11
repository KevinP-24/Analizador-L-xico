from errores import ErrorLexico
from utils.tokens import TokenType

# Importar AFDs individuales
from AFDs.afd_identificador import AFDIdentificador
from AFDs.numero_real import AFDNumeroReal
from AFDs.numero_natural import AFDNumeroNatural
from AFDs.operador_aritmetico import AFDAritmetico
from AFDs.operador_comparacion import AFDComparacion
from AFDs.operador_logico import AFDLogico
from AFDs.operador_asignacion import AFDAtribucion
from AFDs.operador_incremento import AFDIncremento
from AFDs.palabra_reservada import AFDPalabraReservada
from AFDs.parentesis import AFDParentesis
from AFDs.llave import AFDLlave
from AFDs.terminal import AFDTerminal
from AFDs.separador import AFDSeparador
from AFDs.cadena import AFDCadenaCaracteres
from AFDs.comentario import AFDComentario


class Lexer:
    def __init__(self):
        # Orden estratégico: primero tokens más largos o prioritarios
        self.afds = [
            AFDCadenaCaracteres(),
            AFDComentario(),
            AFDPalabraReservada(),
            AFDIdentificador(),
            AFDNumeroReal(),
            AFDNumeroNatural(),
            AFDIncremento(),
            AFDComparacion(),
            AFDLogico(),
            AFDAritmetico(),
            AFDAtribucion(),
            AFDParentesis(),
            AFDLlave(),
            AFDSeparador(),
            AFDTerminal()
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
                        'categoria': categoria.value,  # para mostrar texto descriptivo
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
