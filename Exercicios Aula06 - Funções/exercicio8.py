'''Escreva um programa, com uma função para ler a idade de uma pessoa e
informar a sua classe eleitoral, conforme:
Não-eleitor – abaixo de 16 anos;
Eleitor obrigatório – entre 18 e 65 anos;
Eleitor facultativo – entre 16 e 18 ou maior de 65 anos.'''

def eleitor(idade):
    if idade < 16:
        return "Não-eleitor"
    elif idade >= 18 and idade <= 65:
        return "Eleitor Obrigatório"
    elif idade >= 16 and idade < 18 or idade > 65:
        return "Eleitor Facultativo"

print(eleitor(15))
print(eleitor(18))
print(eleitor(65))
print(eleitor(67))
