# Exercio Hipotenusa
from math import pow
from math import sqrt

print("---- Olá! Iremos fazer o cálculo da Hipotenusa! ----")

Cateto_1 = float(input("Insira o valor do primeiro cateto em cm: "))
Cateto_2 = float(input("Insira o valor do segundo cateto em cm: "))

Hipot = sqrt(pow(Cateto_1, 2) + pow(Cateto_2, 2))

print("-"*40)

print("O valor da hipotenusa é de {:.2f} cm.".format(Hipot))

print("-"*40)
print("Calculo Finalizado!")
print("Encerrando...")



