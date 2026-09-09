import math

print("1 - Hipotenusa")
print("2 - Cateto")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    cateto1  = float(input("Digite o primeiro cateto: "))
    cateto2 = float(input("Digite o segundo cateto: "))

    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print("Hipotenusa =", hipotenusa)

elif opcao == 2:
    hipotenusa = float(input("Digite a hipotenusa: "))
    cateto =float(input("Digite o cateto: "))

    Resultado = math.sqrt(hipotenusa**2 - cateto**2)

    print("Cateto =", Resultado)

else:
    print("Opção inválida.")