valor = float(input("Digite o valor do empréstimo: "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
meses = int(input("Digite a quantidade de meses: "))

juros = valor * (taxa / 100) * meses
montante = valor + juros

print("Juros pagos: R$", juros)
print("Montante total: R$", montante)