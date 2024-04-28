'''Faça um programa com uma função que receba dois números e retorne True
se o primeiro for múltiplo do segundo.'''

def multiplo(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

print(multiplo(100, 10))
print(multiplo(9, 3))
print(multiplo(2, 7))
