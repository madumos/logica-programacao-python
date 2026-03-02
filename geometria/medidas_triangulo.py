import math

l1 = float(input('Qual o tamanho do primeiro lado?'))
l2 = float(input('Qual o tamanho do segundo lado?'))
l3 = float(input('Qual o tamanho do terceiro lado?'))

def e_triangulo(a,b,c): 
     
     if (a + b > c) and  (a + c > b) and (b + c > a):

        if a == b == c:
             print('Este triângulo é equilátero.')

        elif a == b or a == c or c == b:
            print('Este triângulo é isóceles.')
        
        else:
             print('Este triângulo é escaleno.')

        if pow(a,2) + pow(b,2) == pow(c,2) or pow(a,2) + pow(c,2) == pow(b,2) or pow(c,2) + pow(b,2) == pow(a,2):
             print('E também é retângulo!')
        
     else:
          print ('Estas medidas não formam um triângulo.')


e_triangulo(l1,l2,l3)