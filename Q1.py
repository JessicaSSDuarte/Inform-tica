#Entradas
Horas = int(input("Digite a quantidade de Horas: " ))
Minutos = int(input("Digite a quantidade de Minutos: "))
Segundos = (Horas* 3600) + (Minutos*60)
print(f"Tempo total em segundos: {Segundos}s")