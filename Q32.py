peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

print("IMC:", imc)

if imc < 18.5:
    print("Abaixo do peso, xiii ta ruim")
elif imc < 25:
    print("Peso normal, ta de boa")
elif imc < 30:
    print("Sobrepeso, vamo observar")
else:
    print("Obesidade, ta puxada em!!")