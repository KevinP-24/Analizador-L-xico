import sys
import os

# Agrega la carpeta 'automatas' al path de búsqueda de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'automatas'))

from afd import AFD
from lexer import analizar

codigo_scala = '''
// Ejemplo Scala
val x: Int = 10
val mensaje = "Hola mundo"
if (x > 5) println(mensaje)
'''

# Análisis léxico
resultado = analizar(codigo_scala)

for tipo, valor in resultado:
    print(f"{tipo}: {valor}")

# Prueba del AFD para identificadores
afd = AFD()
identificadores = ["mensaje", "x", "_nombre", "9var", "val@", "contador1"]

print("\n--- Validación con AFD ---")
for ident in identificadores:
    resultado = afd.validar(ident)
    print(f"{ident}: {'VÁLIDO' if resultado else 'INVÁLIDO'}")


sys.path.append(os.path.join(os.path.dirname(__file__), 'automatas'))
from afn import AFN

afn = AFN()
cadenas = ["a", "b", "ab", "ba", "abc", "", "c"]

print("\n--- Validación con AFN ---")
for cadena in cadenas:
    resultado = afn.validar(cadena)
    print(f"{cadena!r}: {'ACEPTADA' if resultado else 'RECHAZADA'}")

afd.dibujar()
