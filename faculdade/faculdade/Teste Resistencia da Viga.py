Peso_Maximo = int(input("Insira o peso máximo que a viga suporta em Kg: "))

for Peso_Atual in range(0, Peso_Maximo + 1, 100):
    print(f"Peso Atual: {Peso_Atual} kg... viga estável")

    if Peso_Atual == Peso_Maximo:
        print("ATENÇÃO: Limite de carga atingido!")

print("Teste de estresse finalizado.")

