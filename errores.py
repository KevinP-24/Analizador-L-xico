# errores.py

class ErrorLexico(Exception):
    def __init__(self, mensaje, linea, columna):
        super().__init__(f"[Línea {linea}, Columna {columna}] Error léxico: {mensaje}")
        self.linea = linea
        self.columna = columna
        self.mensaje = mensaje
