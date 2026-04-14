from math import pi
Diam = float(input("Digite o valor do diâmetro do tubo em centímetros: "))
Vel_Vaz = float(input("Digite o velocidade do fluxo m/s: "))

Vazao_Vol = ((pi * (Diam**2)/4) * Vel_Vaz)

print("A velocidade de vazão do fluido é de {:.2f} m/s".format(Vazao_Vol))
