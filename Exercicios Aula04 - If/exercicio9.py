'''Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou
igual a zero e o quadrado do número caso ele seja negativo.'''

import math

numero = float(input("Digite um numero: "))

if numero >= 0:
    n1 = math.sqrt(numero)
    print(f"Raiz quadrada: {n1:.2f}") 
else:
    n1 = numero ** 2
    print(f"Quadrada: {n1:.2f}")
