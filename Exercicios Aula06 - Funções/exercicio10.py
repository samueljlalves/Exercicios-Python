''''Escreva um programa, com uma função que leia 2 valores (A e B), calcule
e mostre a soma dos números ímpares entre eles (inclusive A e B). Nesse
caso, considere que só serão informados valores inteiros positivos e que A é
menor que B.'''

i = 0

def somaImpar(a, b):
    acum = 0
    for i in range (a, b):
        if i % 2 != 0:
            acum = acum + i

        i += 1 

    return "Soma: %d" % acum


a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

if a > 0 and a < b and b > 0:
    print(somaImpar(a, b))
else:
    print("Digite apenas numeros inteiros e positivos.")