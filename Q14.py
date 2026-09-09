preco = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))
desconto = float(input("Digite o desconto em reais: "))

total = (preco * quantidade) - desconto

print("Valor final da compra: R$", total)