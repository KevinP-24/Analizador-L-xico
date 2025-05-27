from graphviz import Digraph

def generar_afd_aritmetico():
    dot = Digraph(comment='AFD Operadores Aritméticos')
    dot.attr(rankdir='LR', ranksep='1.2', nodesep='0.8')
    dot.attr('node', fontsize='14', margin='0.3')
    dot.attr('edge', fontsize='12')

    dot.node('0', 'q0', shape='circle')
    dot.node('1', 'q1', shape='doublecircle')

    dot.edge('0', '1', label='+ - * / %')

    dot.render('afd_aritmetico', format='png', cleanup=False)
    print("✅ Imagen generada: afd_aritmetico.png")

if _name_ == '_main_':
    generar_afd_aritmetico()