'''Faça um Programa que calcule o peso ideal de uma pessoa. Para isso, solicite a
altura da pessoa, o nome da pessoa. Utilize as seguintes fórmulas:

Homens – (72.7 * altura) – 58

Mulheres – (62.1 * altura) – 44.7 '''

altura = float(input("Digite sua altura: "))
nome = input("Digite seu nome: ")

homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

print("O peso ideal para homens é:", homens)
print("O peso ideal para mulheres é:", mulheres)
