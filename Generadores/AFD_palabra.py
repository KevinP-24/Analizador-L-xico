from graphviz import Digraph

def generar_afd_palabra_reservada():
    dot = Digraph(comment='AFD Palabras Reservadas')
    dot.attr(rankdir='LR', ranksep='1.2', nodesep='0.8')
    dot.attr('node', fontsize='14', margin='0.3')
    dot.attr('edge', fontsize='12')

    for i in range(26):
        forma = 'doublecircle' if i in {2, 6, 11, 14, 20, 25} else 'circle'
        dot.node(str(i), f'q{i}', shape=forma)

    # "if"
    dot.edge('0', '1', label='i')
    dot.edge('1', '2', label='f')

    # "else"
    dot.edge('0', '3', label='e')
    dot.edge('3', '4', label='l')
    dot.edge('4', '5', label='s')
    dot.edge('5', '6', label='e')

    # "while"
    dot.edge('0', '7', label='w')
    dot.edge('7', '8', label='h')
    dot.edge('8', '9', label='i')
    dot.edge('9', '10', label='l')
    dot.edge('10', '11', label='e')

    # "def"
    dot.edge('0', '12', label='d')
    dot.edge('12', '13', label='e')
    dot.edge('13', '14', label='f')

    # "return"
    dot.edge('0', '15', label='r')
    dot.edge('15', '16', label='e')
    dot.edge('16', '17', label='t')
    dot.edge('17', '18', label='u')
    dot.edge('18', '19', label='r')
    dot.edge('19', '20', label='n')

    # "class"
    dot.edge('0', '21', label='c')
    dot.edge('21', '22', label='l')
    dot.edge('22', '23', label='a')
    dot.edge('23', '24', label='s')
    dot.edge('24', '25', label='s')

    dot.render('afd_palabra_reservada', format='png', cleanup=False)
    print("✅ Imagen generada: afd_palabra_reservada.png")

if _name_ == '_main_':
    generar_afd_palabra_reservada()