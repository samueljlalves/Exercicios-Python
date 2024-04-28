'''Escreva um programa que leia dois números e que pergunte qual a operação
você deseja realizar: soma (+), subtração (-), multiplicação (*) e divisão (/).
Exiba o resultado da operação realizada. Use o comando if.'''

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

op = input("Qual operação deseja fazer? ")

if op == "+":
    res = n1 + n2
    print("O valor da soma é:", res)
elif op == "-":
    res = n1 - n2
    print("O valor da subtração é:", res)
elif op == "*":
    res = n1 * n2
    print("O valor da multipricação é:", res)
elif op == "/":
    res = n1 / n2
    print("O valor da divisão é:", res)
else:
    print("Operação invalida")
