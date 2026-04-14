from math import pi
raio = float(input("Digite o valor do raio de um circulo em centímetros: "))
per = pi*raio*2
area = pi*raio**2

print("O circulo possui uma área igual a {:.2f} cm² e um perímetro igual a {:.2f} cm".format(area, per))
