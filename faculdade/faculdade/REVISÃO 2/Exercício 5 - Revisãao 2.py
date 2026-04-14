# Exercício de cálculo de circulo
from math import pi
from fractions import Fraction

Nume = int(input("Insira o numerador da fração: "))
Deno = int(input("Insira o denominador da fração: "))

raio = Fraction(Nume, Deno)

if Nume < 0 or Deno <= 0:
    print("Erro: valores inválidos.")

else:
    raio = Nume / Deno
    area = pi * (raio**2)
    print("A área do círculo de raio {:.2f} unidades é {:.6f} unidades².".format(raio, area))
    
