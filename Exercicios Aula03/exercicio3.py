'''Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor
do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo
salário. Para exemplo, teste a porcentagem de aumento de 5%.'''

salario = float(input("Digite seu salario: "))
aumento = float(input("Digite o valor de aumento: "))

valoraumento = salario / 100 * aumento

novosalario = valoraumento + salario

print("O valor aumentado é: R$" "%.2f" %valoraumento)
print("Seu novo salario é: R$" "%.2f" %novosalario)
