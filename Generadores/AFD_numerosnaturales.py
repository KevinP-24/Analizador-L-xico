from graphviz import Digraph

def generar_afd_numero_natural():
    dot = Digraph(comment='AFD Número Natural')
    dot.attr(rankdir='LR', ranksep='1.2', nodesep='0.8')
    dot.attr('node', fontsize='14', margin='0.3')
    dot.attr('edge', fontsize='12')

    dot.node('0', 'q0', shape='circle')
    dot.node('1', 'q1', shape='doublecircle')

    dot.edge('0', '1', label='dígito')
    dot.edge('1', '1', label='dígito')

    dot.render('afd_numero_natural', format='png', cleanup=False)
    print("✅ Imagen generada: afd_numero_natural.png")

if _name_ == '_main_':
    generar_afd_numero_natural()