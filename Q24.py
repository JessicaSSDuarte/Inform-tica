v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
v3 = float(input("Digite o terceiro valor: "))
v4 = float(input("Digite o quarto valor: "))
v5 = float(input("Digite o quinto valor: "))

soma = 0
quantidade = 0

if v1 > 0 and v1 < 1000:
    soma += v1
    quantidade += 1

if v2 > 0 and v2 < 1000:
    soma += v2
    quantidade += 1

if v3 > 0 and v3 < 1000:
    soma += v3
    quantidade += 1

if v4 > 0 and v4 < 1000:
    soma += v4
    quantidade += 1

if v5 > 0 and v5 < 1000:
    soma += v5
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print("Média das medições válidas:", media)
else:
    print("Nenhuma medição válida.")