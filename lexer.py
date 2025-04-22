import re
from utils.tokens import TOKEN_REGEX


"""
¿Qué hace esta función?
Recorre el texto carácter por carácter.
Intenta hacer match con cada tipo de token definido.
Si lo encuentra, lo agrega a la lista (tokens_encontrados) con su tipo y valor.
Si encuentra espacios (WHITESPACE), los ignora.
Si no encuentra ningún token válido, lanza un error.
"""
def analizar(texto):
    tokens_encontrados = []
    posicion = 0
    while posicion < len(texto):
        match = None
        for tipo, patron in TOKEN_REGEX.items():
            regex = re.compile(patron)
            match = regex.match(texto, posicion)
            if match:
                valor = match.group()
                if tipo != 'WHITESPACE':  # Ignorar espacios
                    tokens_encontrados.append((tipo, valor))
                posicion = match.end()
                break
        if not match:
            raise SyntaxError(f"Token no reconocido en: '{texto[posicion:]}'")
    return tokens_encontrados


