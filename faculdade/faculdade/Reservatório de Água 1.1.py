import math
continuar = 's'
while continuar.lower() == 's':
    print("\n--- Novo Cálculo de Reservatório ---")

    Diametro_Reservatorio = float(input("Insira o valor do diametro do reservatorio  em metros"))
    Altura_Reservatorio = float(input("Insira o valor da altura do reservatório em metros"))
    Preco_Agua = float(input("Insira o preço da água em metros cubicos"))
    Quantidade_de_Agua_Comprada = float(input("Insira a quantidade de água comprada em m³"))

    Raio_Reservatorio = Diametro_Reservatorio/2
    Area_Base_Reservatorio = math.pi*(Raio_Reservatorio**2)
    Volume_Reservatorio = Area_Base_Reservatorio*Altura_Reservatorio
    Custo_Total = Volume_Reservatorio*Preco_Agua

    if Quantidade_de_Agua_Comprada > Volume_Reservatorio:
        print("Vai transbordar!")
    elif Quantidade_de_Agua_Comprada > Volume_Reservatorio*0.90:
        print("Volume acima da capacidade de segurança!")
    else:
        print("Cabe, não apresenta risco de transbordar!")

    print(f"O valor total para encher o reservatório será de R${Custo_Total:.2f}")

    continuar = input("\nDeseja calcular outro reservatório? (s/n): ")

print("\nObrigado por usar o sistema! Encerrando...")

