from graphviz import Digraph

def generar_afd_identificador():
    dot = Digraph(comment='AFD Identificador')
    dot.attr(rankdir='LR', ranksep='1.2', nodesep='0.8')
    dot.attr('node', fontsize='14', margin='0.3')
    dot.attr('edge', fontsize='12')

    # Estados
    dot.node('0', 'q0', shape='circle')
    dot.node('1', 'q1', shape='doublecircle')

    # Transiciones
    dot.edge('0', '1', label='letra | _')
    dot.edge('1', '1', label='letra | dígito | _')

    # Generar imagen
    nombre_archivo = 'afd_identificador'
    dot.render(nombre_archivo, format='png', cleanup=False)
    print(f"✅ Imagen generada: {nombre_archivo}.png")

if _name_ == '_main_':
    generar_afd_identificador()