Valor_do_Lado = float(input("Insira o valor do lado"))
import math

Area_Triangulo = ((Valor_do_Lado**2)*math.sqrt(3)/4)
Area_Hexagono = Area_Triangulo*6

print(f"O valor da area do Hexagono é:{Area_Hexagono:.2f}cm²")
                  
