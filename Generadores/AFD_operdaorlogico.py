from graphviz import Digraph

def generar_afd_logico():
    dot = Digraph(comment='AFD Operadores Lógicos')
    dot.attr(rankdir='LR', ranksep='1.2', nodesep='0.8')
    dot.attr('node', fontsize='14', margin='0.3')
    dot.attr('edge', fontsize='12')

    dot.node('0', 'q0', shape='circle')
    dot.node('1', 'q1', shape='circle')
    dot.node('2', 'q2', shape='doublecircle')

    dot.edge('0', '1', label='& o |')
    dot.edge('1', '2', label='& o |')
    dot.edge('0', '2', label='!')

    dot.render('afd_logico', format='png', cleanup=False)
    print("✅ Imagen generada: afd_logico.png")

if _name_ == '_main_':
    generar_afd_logico()