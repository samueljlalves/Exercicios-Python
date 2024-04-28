'''Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

Calcule e mostre o total de seu salário total no referido mês, sabendo-se que são descontados 11% para o
imposto de renda, 8% para o INSS e 5% para o sindicato. Faça com que o programa que nos dê: salário
bruto, quanto pagou de INSS, quanto pagou de IR, quanto pagou de sindicato e o salário líquido, conforme
tabela abaixo:
+ Salário Bruto: R$
IR (11%): R$
INSS (8%): R$
Sindicato (5%): R$
= Salário líquido: R$ .'''

valorhora = float(input("Digite o valor da sua hora: "))
qtdhora = float(input("Digite quantas horas mensais: "))

salario = qtdhora * valorhora
ir = salario / 100 * 11
inss = salario / 100 * 8
sindicato = salario / 100 * 5

salarioliquido = salario - (ir + inss + sindicato)

print(f"Salario Bruto: {salario:.2f}")
print(f"IR (11%): R$: {ir:.2f}")
print(f"INSS (8%): R$: {inss:.2f}")
print(f"Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salario Liquido: R$ {salarioliquido:.2f}")
