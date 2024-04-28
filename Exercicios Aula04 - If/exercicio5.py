'''Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para
residências, I para indústrias e C para comércios. Calcule o preço a pagar, de acordo
com a tabela a seguir:'''

kwh = float(input("Digite quantos kWh consumido: "))
tipo = input("Digite o tipo de instalação (r) para residencial, (c) para comercial e (i) para industrial: ")

if (tipo == "r" or tipo == "R") and kwh <= 500:
    preco = kwh * 0.40
    print("O valor a se pagar é: R$ 0,40 por kwh.")
    print("Valor a pagar:", preco)
elif (tipo == "r" or tipo == "R") and kwh <= 1000:
    preco = kwh * 0.65
    print("O valor a se pagar é: R$ 0,65 por kwh.")
    print("Valor a pagar:", preco)
elif (tipo == "c" or tipo == "C") and kwh <= 2500:
    preco = kwh * 0.55
    print("O valor a se pagar é: R$ 0,55 por kwh.")
    print("Valor a pagar:", preco)
elif (tipo == "c" or tipo == "C") and kwh <= 5000:
    preco = kwh * 0.60
    print("O valor a se pagar é: R$ 0,60 por kwh.")
    print("Valor a pagar:", preco)
elif (tipo == "i" or tipo == "I") and kwh <= 10000:
    preco = kwh * 0.55
    print("O valor a se pagar é: R$ 0,55 por kwh.")
    print("Valor a pagar:", preco)
elif (tipo == "i" or tipo == "I") and kwh <= 15000:
    preco = kwh * 0.60
    print("O valor a se pagar é: R$ 0,60 por kwh.")
    print("Valor a pagar:", preco)
else:
    print("Valor invalido")

    

