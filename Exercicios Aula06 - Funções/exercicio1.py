'''Faça um programa com uma função que retorne o maior de dois números.'''

def maior(n1, n2):
    if n1 > n2:
        maior = n1
        return("Maior: %d" % n1)
    else:
        return("Maior: %d" % n2)

print(maior(1 ,2))
print(maior(90 ,100))
      
