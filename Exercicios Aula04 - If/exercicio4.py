'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade
de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do
salário. Calcule o valor da prestação como sendo, o valor da casa a comprar
dividido pelo número de meses a pagar.'''

valorcasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
vezes = int(input("Digite em quantas vezes deseja pagar: "))

prestacao = valorcasa / vezes
aprovacao = salario / 100 * 30

if prestacao <= aprovacao:
    print(f"Valor das prestações: {prestacao:.2f}")
    print("Valor das parcelas:", vezes)
else:
    print("Valor de emprestimo não aprovado")
