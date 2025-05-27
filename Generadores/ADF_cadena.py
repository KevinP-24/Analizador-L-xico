from graphviz import Digraph

def generar_afd_cadena():
    dot = Digraph(comment='AFD Cadenas de Caracteres')
    dot.attr(rankdir='LR', ranksep='1.2', nodesep='0.8')
    dot.attr('node', fontsize='14', margin='0.3')
    dot.attr('edge', fontsize='12')

    # Estados
    dot.node('0', 'q0', shape='circle')            # inicio
    dot.node('1', 'q1', shape='circle')            # dentro de la cadena
    dot.node('2', 'q2', shape='doublecircle')      # aceptación

    # Transiciones
    dot.edge('0', '1', label='"')
    dot.edge('1', '1', label='carácter válido')
    dot.edge('1', '1', label='\\ + cualquier')
    dot.edge('1', '2', label='"')

    # Generar imagen
    nombre_archivo = 'afd_cadena'
    dot.render(nombre_archivo, format='png', cleanup=False)
    print(f"✅ Imagen generada: {nombre_archivo}.png")

if _name_ == '_main_':
    generar_afd_cadena()