Diametro_Reservatorio = float(input("Insira o valor do diametro do reservatorio  em metros"))
Altura_Reservatorio = float(input("Insira o valor da altura do reservatório em metros"))
Preco_Agua = float(input("Insira o preço da água em metros cubicos"))
import math

Raio_Reservatorio = Diametro_Reservatorio/2
Area_Base_Reservatorio = math.pi*(Raio_Reservatorio**2)
Volume_Reservatorio = Area_Base_Reservatorio*Altura_Reservatorio
Custo_Total = Volume_Reservatorio*Preco_Agua

print(f"O valor total para encher o reservatório será de R${Custo_Total:.2f}")

