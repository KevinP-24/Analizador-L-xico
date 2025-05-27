from graphviz import Digraph

def generar_afd_comentario():
    dot = Digraph(comment='AFD Comentarios')
    dot.attr(rankdir='LR', ranksep='1.2', nodesep='0.8')
    dot.attr('node', fontsize='14', margin='0.3')
    dot.attr('edge', fontsize='12')

    # Estados
    dot.node('0', 'q0', shape='circle')
    dot.node('1', 'q1', shape='circle')
    dot.node('2', 'q2', shape='doublecircle')  # comentario de línea aceptado
    dot.node('3', 'q3', shape='circle')
    dot.node('4', 'q4', shape='doublecircle')  # comentario de bloque aceptado

    # Transiciones
    dot.edge('0', '1', label='/')
    dot.edge('1', '2', label='/ ... \\n')
    dot.edge('1', '3', label='*')
    dot.edge('3', '3', label='contenido')
    dot.edge('3', '4', label='*/')

    # Generar imagen
    nombre_archivo = 'afd_comentario'
    dot.render(nombre_archivo, format='png', cleanup=False)
    print(f"✅ Imagen generada: {nombre_archivo}.png")

if _name_ == '_main_':
    generar_afd_comentario()