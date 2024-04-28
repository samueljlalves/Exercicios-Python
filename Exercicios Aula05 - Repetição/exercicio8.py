'''Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar

[2] multiplicar

[3] maior

[4] menor

[5] dividir

[6] subtrair

[7] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

menu = int(input("[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Menor\n[5]Dividir\n[6]Subtrair\n[7]Sair do programa\n"))

if menu == 1:
    res = n1 + n2
    print("A soma é:", res)
    
elif menu == 2:
    res = n1 * n2
    print("A multiplicação e:", res)
    
elif menu == 3:
    if n1 > n2:
        print("O maior numero é:", n1)

    else:
        print("O maior numero é:", n2)
        
elif menu == 4:
    if n1 > n2:
        print("O menor numero é:", n2)
    else:
        print("O menor numero é:", n1)
        
elif menu == 5:
    res = n1 / n2
    print("A divisão é:", res)
    
elif menu == 6:
    res = n1 - n2
    print("A divisão é:", res)
    
elif menu == 7:
    print("Você saiu do programa")
    
