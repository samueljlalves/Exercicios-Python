'''Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar,
desconsidere-o.'''

x = 1
soma = 0

while x <= 6:
    numero = int(input("Digite seis numeros: "))
    if numero % 2 == 0:
        soma = soma + numero
    x += 1
    
print("A soma dos numeros pares é:", soma)
    
    
