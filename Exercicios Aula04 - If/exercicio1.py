'''Escreva um programa que pergunte a velocidade do carro de um usuário. Caso
ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse
caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 80 km/h.'''

velocidade = int(input("Digite a velocidade: "))

if velocidade > 80:
    acima = velocidade - 80
    multa = acima * 5
    print("O valor da multa a pagar é: ", multa)
else:
    print("Você não ultrapassou o limite de velocidade")
