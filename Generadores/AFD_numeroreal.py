from graphviz import Digraph

def generar_afd_numero_real():
    dot = Digraph(comment='AFD Número Real')
    dot.attr(rankdir='LR', ranksep='1.2', nodesep='0.8')
    dot.attr('node', fontsize='14', margin='0.3')
    dot.attr('edge', fontsize='12')

    dot.node('0', 'q0', shape='circle')
    dot.node('1', 'q1', shape='circle')
    dot.node('2', 'q2', shape='circle')
    dot.node('3', 'q3', shape='doublecircle')

    dot.edge('0', '1', label='dígito')
    dot.edge('1', '1', label='dígito')
    dot.edge('1', '2', label='.')
    dot.edge('2', '3', label='dígito')
    dot.edge('3', '3', label='dígito')

    dot.render('afd_numero_real', format='png', cleanup=False)
    print("✅ Imagen generada: afd_numero_real.png")

if _name_ == '_main_':
    generar_afd_numero_real()