'''Crie um programa que mostre na tela todos os números pares no intervalo
entre 1 e 50.'''

x = 1
cont = 0

while x <= 50:
    if x % 2 == 0:
        cont += 1
        print(x)
    x += 1
