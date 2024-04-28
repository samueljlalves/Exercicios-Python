'''Faça um programa com uma função chamada somaImposto. A função
possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
sobre vendas expressa em porcentagem e, custo, que é o custo de um item
antes do imposto. A função “altera” o valor de custo para incluir o imposto
sobre vendas.'''

def somaImposto(taxaImposto, custo):
    altera = custo / 100 * taxaImposto
    valor = custo - altera
    return "Valor alterado: %d" % valor

taxaImposto = float(input("Informe a taxa de Imposto: "))
custo = float(input("Informe o custo: "))

print("\n" , somaImposto(taxaImposto, custo))