num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

operacao = input("Digite a operação (+, -, * ou /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    resultado = "Operação inválida."

print("Resultado:", resultado)