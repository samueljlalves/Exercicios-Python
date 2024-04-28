'''Faça um programa que solicite o preço de uma mercadoria e o percentual de
desconto. Exiba o valor do desconto e o preço a pagar.'''

valor = float(input("Digite o valor do da mercadoria: "))
desconto = float(input("Digite o valor em desconto: "))

valordesconto = valor / 100 * desconto
precopagar = valor - valordesconto

print("O valor de desconto é: " "%.2f" %valordesconto)
print("Total a se pagar: " "%.2f" %precopagar)

