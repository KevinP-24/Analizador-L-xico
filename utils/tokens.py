import re

# Diccionario con tipos de tokens y sus expresiones regulares
TOKEN_REGEX = {
    'KEYWORD': r'\b(if|else|while|return)\b',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z_0-9]*\b',
    'NUMBER': r'\b\d+(\.\d+)?\b',
    'OPERATOR': r'==|!=|<=|>=|[+\-*/=]',
    'STRING': r'"[^"]*"|\'[^\']*\'',
    'PAREN': r'[\(\)]',
    'BRACE': r'[\{\}]',
    'SEMICOLON': r';',
    'COMMA': r',',
    'WHITESPACE': r'\s+',
}