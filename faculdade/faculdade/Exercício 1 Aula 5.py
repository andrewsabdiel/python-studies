# Exercicio Plano Cartesiano
from math import sqrt
from math import pow

print("-"*40)
print("Vamos inserir os valores do primeiro ponto:")
x1 = float(input("Coloque o valor de X do P1: "))
y1 = float(input("Coloque o valor de Y do P1: "))

print("-"*40)
print("Vamos inserir os valores do segundo ponto:")
x2 = float(input("Coloque o valor de X do P2: "))
y2 = float(input("Coloque o valor de Y do P2: "))

calculo = sqrt((pow((x2 - x1), 2)) + (pow((y2 - y1), 2)))
print("-"*40)
print("A distancia entre os dois pontos é: {:.2f}".format(calculo))
print("-"*40)
print("Processo Finalizado!")
print("Desligando...")

