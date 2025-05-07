from graphviz import Digraph
import os

class AFD:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceptacion = {'q1'}
        self.transiciones = {
            'q0': {'letra': 'q1', 'guion_bajo': 'q1'},
            'q1': {'letra': 'q1', 'digito': 'q1', 'guion_bajo': 'q1'},
        }

    def tipo_char(self, char):
        if char.isalpha():
            return 'letra'
        elif char.isdigit():
            return 'digito'
        elif char == '_':
            return 'guion_bajo'
        else:
            return 'otro'

    def validar(self, cadena):
        estado_actual = self.estado_inicial
        for caracter in cadena:
            tipo = self.tipo_char(caracter)
            if tipo not in self.transiciones.get(estado_actual, {}):
                return False
            estado_actual = self.transiciones[estado_actual][tipo]
        return estado_actual in self.estados_aceptacion

    def dibujar(self, nombre="afd_identificadores"):
        dot = Digraph(comment="AFD Identificadores")

        # Estados
        for estado in set(self.transiciones.keys()).union(*[set(v.values()) for v in self.transiciones.values()]):
            forma = 'doublecircle' if estado in self.estados_aceptacion else 'circle'
            dot.node(estado, shape=forma)

        # Estado inicial
        dot.node('start', '', shape='point')
        dot.edge('start', self.estado_inicial)

        # Agrupar transiciones por (origen → destino)
        transiciones_agrupadas = {}
        for origen, trans in self.transiciones.items():
            for simbolo, destino in trans.items():
                clave = (origen, destino)
                if clave not in transiciones_agrupadas:
                    transiciones_agrupadas[clave] = []
                transiciones_agrupadas[clave].append(simbolo)

        # Dibujar transiciones agrupadas
        for (origen, destino), simbolos in transiciones_agrupadas.items():
            etiqueta = ", ".join(simbolos)
            dot.edge(origen, destino, label=etiqueta)

        output_path = os.path.join(os.path.dirname(__file__), f"{nombre}.gv")
        dot.render(output_path, format='png', cleanup=True)
        print(f"✅ AFD dibujado y guardado como: {output_path}.png")
