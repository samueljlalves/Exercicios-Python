'''Faça um programa com uma função que necessite de uma argumento. A
função retorna o valor do caractere ‘P’, se o seu argumento for positivo, e
‘N’, se o ser argumento for zero ou negativo.'''

def arg(numero):
    if numero > 0:
        return "P"
    else:
        return "N"
print(arg(10))
print(arg(0))
      
    
