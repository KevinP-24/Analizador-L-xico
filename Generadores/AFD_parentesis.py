from graphviz import Digraph

def generar_afd_parentesis():
    """
    Genera el AFD para reconocer paréntesis de apertura y cierre: ( y )
    """
    dot = Digraph(comment='AFD Paréntesis')
    dot.attr(rankdir='LR', ranksep='1.2', nodesep='0.8')
    dot.attr('node', fontsize='14', margin='0.3')
    dot.attr('edge', fontsize='12')

    dot.node('0', 'q0', shape='circle')
    dot.node('1', 'q1', shape='doublecircle')

    dot.edge('0', '1', label='( o )')

    dot.render('afd_parentesis', format='png', cleanup=False)
    print("✅ Imagen generada: afd_parentesis.png")

if _name_ == '_main_':
    generar_afd_parentesis()