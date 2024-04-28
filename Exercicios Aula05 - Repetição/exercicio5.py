'''Faça um programa que mostre a tabuada de um número que o usuário
escolher utilizando um laço for.'''

numero = int(input("Escolha umn numero: "))

for i in range(1, 11):
    x = numero * i
    print(numero,"x", i, "=", x)
