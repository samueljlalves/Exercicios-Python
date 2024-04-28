'''Faça um programa em Python que receba um valor de uma compra. Testar se o
cliente gastou até R$ 100,00, deve pagar em dinheiro. Se gastou entre R$ 100,00 e
R$ 300,00, deve pagar no cartão de débito. Se gastou acima de R$ 300,00, pode
pagar no cartão de crédito.'''

pagamento = float(input("Digite o valor da compra: "))

if pagamento <= 100:
    print("O pagamento deve ser em dinheiro")
elif pagamento > 100 and pagamento <= 300:
    print("O pagamento deve ser em cartão de Débito")
else:
    print("O pagamento poderá ser pago com cartão de credito")
