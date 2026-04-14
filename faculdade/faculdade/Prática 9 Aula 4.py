from math import pi
from math import pow
raio_ext = float(input("Digite o valor do raio externo da coroa em cm: "))
raio_int = float(input("Digite o valor do raio interno da coroa em cm: "))

Area_Cil = pi*(pow(raio_ext,2))
Area_vaz = pi*(pow(raio_int,2))
Area_coroa = Area_Cil - Area_vaz

print("A área da coroa circular apresenta o valor de {:.2f} cm²".format(Area_coroa))
