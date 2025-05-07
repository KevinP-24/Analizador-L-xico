import re
from utils.tokens import TOKEN_REGEX

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
                # Ignorar espacios y opcionalmente comentarios
                if tipo not in ['WHITESPACE', 'COMMENT']:
                    tokens_encontrados.append((tipo, valor))
                posicion = match.end()
                break

        if not match:
            raise SyntaxError(f"Token no reconocido en: '{texto[posicion:]}'")

    return tokens_encontrados
