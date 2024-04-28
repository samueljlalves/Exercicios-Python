'''Faça um programa que calcule a soma entre todos os números que são
múltiplos de três e que se encontram no intervalo de 1 até 500.'''

x = 1
cont = 0

while x <= 500:
    if x % 3 == 0:
        cont += 1
        print(x)
    x += 1
    

