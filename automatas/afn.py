class AFN:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}
        self.estado_inicial = 'q0'
        self.estados_aceptacion = {'q1', 'q2'}
        self.transiciones = {
            'q0': {'a': ['q1'], 'b': ['q2']},
            'q1': {'a': ['q1'], 'b': ['q2']},
            'q2': {'b': ['q2'], 'a': ['q1']}
        }

    def validar(self, cadena):
        actuales = [self.estado_inicial]

        for caracter in cadena:
            siguientes = []
            for estado in actuales:
                if caracter in self.transiciones.get(estado, {}):
                    siguientes.extend(self.transiciones[estado][caracter])
            if not siguientes:
                return False
            actuales = siguientes

        return any(estado in self.estados_aceptacion for estado in actuales)
