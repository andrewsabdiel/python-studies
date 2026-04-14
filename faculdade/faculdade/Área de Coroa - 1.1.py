Raio_Maior = float(input("Insira o valor em cm do raio maior"))
Raio_Menor = float(input("Insira o valor em cm do raio menor"))
import math

Area_da_Coroa = math.pi*((Raio_Maior**2)-(Raio_Menor**2))

print(f"A area da coroa circular será de{Area_da_Coroa:.2f}cm²")
