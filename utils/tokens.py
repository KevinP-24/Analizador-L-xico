from enum import Enum

class TokenType(Enum):
    IDENTIFICADOR = "Identificador"
    NUMERO_NATURAL = "Número Natural"
    NUMERO_REAL = "Número Real"
    OPERADOR_ARITMETICO = "Operador aritmético"
    OPERADOR_COMPARACION = "Operador de comparación"
    OPERADOR_LOGICO = "Operador lógico"
    OPERADOR_ASIGNACION = "Operador de asignación"
    OPERADOR_INCREMENTO = "Operador de incremento"
    CADENA = "Cadena"
    COMENTARIO = "Comentario"
    PARENTESIS = "Paréntesis"
    LLAVE = "Llave"
    SEPARADOR = "Separador"
    TERMINAL = "Fin de sentencia"
    PALABRA_RESERVADA = "Palabra reservada"
    ERROR = "Error"