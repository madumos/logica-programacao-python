
n1 = float(input('Qual a sua nota na primeira prova?'))
n2 = float(input('Qual a sua nota na segunda prova?'))


def media(a,b):
    """
    Retorna a média ponderada das 2 notas
    """
    print(round((0.4*a + 0.6*b)/10,2))

media(n1,n2)



