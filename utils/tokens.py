import re

TOKEN_REGEX = {
    # Palabras clave de Scala
    'KEYWORD': r'\b(if|else|while|for|def|val|var|class|object|match|case|import|new|return|this|super|trait|extends|with|yield|try|catch|finally|throw|override|abstract|sealed|private|protected|final|implicit|lazy|do)\b',

    # Tipos de datos comunes en Scala
    'TYPE': r'\b(Int|String|Boolean|Double|Float|Unit|Any|Nothing|Char|Long|Short|Byte)\b',

    # Literales booleanos
    'BOOLEAN': r'\b(true|false)\b',

    # Null literal
    'NULL': r'\bnull\b',

    # Identificadores
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',

    # Números: enteros y decimales
    'NUMBER': r'\b\d+(\.\d+)?\b',

    # Cadenas de texto: normales y multilínea
    'STRING': r'("""[\s\S]*?"""|"[^"\n]*")',

    # Caracteres
    'CHAR': r"\'[^']\'",

    # Comentarios de línea y bloque
    'COMMENT': r'(//[^\n]*|/\*[\s\S]*?\*/)',

    # Operadores de Scala
    'OPERATOR': r'==|!=|<=|>=|=>|->|:=|[-+*/%=<>!&|^~]+',

    # Anotaciones como @deprecated
    'ANNOTATION': r'@\b[a-zA-Z_][a-zA-Z0-9_]*\b',

    # Paréntesis, llaves y corchetes
    'PAREN': r'[()]',
    'BRACE': r'[\{\}]',
    'BRACKET': r'[\[\]]',

    # Puntuación
    'COMMA': r',',
    'SEMICOLON': r';',
    'DOT': r'\.',

    # Espacios (serán ignorados)
    'WHITESPACE': r'\s+',
    'COLON': r':',
}
