'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do
aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para
inferiores ou iguais, 15%:'''

salario = float(input("Digite seu salario: "))

if salario <= 1250:
    aumento = salario / 100 * 15
    novosalario = salario + aumento
    print("Valor do aumento:", aumento)
    print("Seu salario com aumento será:", novosalario)
else:
    aumento = salario / 100 * 10
    novosalario = salario + aumento
    print("Valor do aumento:", aumento)
    print("Seu salario com aumento será:", novosalario)
