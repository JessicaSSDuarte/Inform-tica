nome = input("Digite o nome: ")
ano = int(input("Digite o ano de nascimento: "))

idade = 2026 - ano

if idade >= 18:
    situacao = "Acesso permitido normalmente."
else:
    situacao = "Acesso permitido somente acompanhado de um responsável."

print("Nome:", nome)
print("Idade:", idade)
print(situacao)