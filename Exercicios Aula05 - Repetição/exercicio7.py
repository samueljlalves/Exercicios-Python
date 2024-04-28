'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
foi o maior e o menor peso lidos.'''

i = 1

while i <= 6:
    peso = float(input("Digite cinco pesos: "))

    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    i+=1

print("O maior peso é:", maior)
print("O menor peso é:", menor)
