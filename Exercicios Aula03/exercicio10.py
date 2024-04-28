'''João, papo de pescador, homem de bem, comprou microcomputador para controlar
o rendimento diário de seu trabalho.

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por
quilo excedente.

João precisa que você faça um programa que leia a variável peso (peso de peixes) e
calcule o excesso.

Gravar na variável excesso a quantidade de quilos além do limite e na variável multa
o valor da multa que João deverá pagar. Imprima os dados do programa com
mensagens adequadas.'''

peso = float(input("Digite o peso total dos peixeis: "))

if (peso <50):
    print("O peso não excedeu os 50 kilos, não pagará multa")

elif (peso > 50):
    excesso = peso - 50
    multa = excesso * 4
    print("O peso excedido é:", excesso)
    print("O valor de multa a se pagar pelo excesso de peso é:", multa)
