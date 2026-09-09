tempo1 = float(input("Digite o tempo do servidor 1: "))
tempo2 = float(input("Digite o tempo do servidor 2: "))
tempo3 = float(input("Digite o tempo do servidor 3: "))
tempo4 = float(input("Digite o tempo do servidor 4: "))

menor = min(tempo1, tempo2, tempo3, tempo4)

print("Menor tempo de resposta:", menor, "ms")