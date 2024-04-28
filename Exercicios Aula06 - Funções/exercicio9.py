'''Escreva um programa, com uma função que imprima o conceito de um
aluno, dada a sua nota. Supor, apenas, notas inteiras. O critério para
conceitos é o seguinte:'''

def conceito(nota):
    if nota < 3:
        return "Conceito E"
    elif nota >= 3 and nota <= 5:
        return "Conceito D"
    elif nota >= 6 and nota <= 7:
        return "Conceito C"
    elif nota >= 8 and nota <= 9:
        return "Conceito B"
    else:
        return "Conceito A"
    
print(conceito(2))
print(conceito(4))
print(conceito(7))
print(conceito(8))
print(conceito(10))