'''Para doar sangue é necessário:

Ter entre 16 e 69 anos.

Pesar mais de 50 kg.

Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).

Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 horas para uma pessoa e
diga se ela por ou não doar sangue.'''

idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
sono = float(input("Digite quanto dormiu nas ultimas 24 horas: "))

if idade >= 16 and idade <= 69 and peso >= 50 and sono >= 6:
    print("Você está habita a doar sangue")
else:
    print("Você não está habito a doar sangue")
