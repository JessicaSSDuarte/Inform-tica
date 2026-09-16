idade = 8
print(type(idade))
altura= 20.00
print(type(altura))
usuário="Jess"
print(type(usuário))
ativo = True
print(type(ativo))

entrada=(input("Digite a mensagem:"))
print("É numerico?",entrada.isnumeric())
print("É alfabético?", entrada.isalpha())
print("É alfanumérico?", entrada.isalnum())
print("É decimal?", entrada.isdecimal())
print("Possui apenas espaços?", entrada.isspace())
print("Está em maiúsculo?", entrada.isupper())
print("Está em minúsculo?", entrada.islower())