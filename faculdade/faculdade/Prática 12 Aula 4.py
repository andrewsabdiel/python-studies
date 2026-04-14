print("Iremos calcular a área de um hexagono regular!")
print("Para isso, preciso dos seguintes valores:")
Raio = float(input("Valor do raio do hexagono em cm: "))
Lado = float(input("Valor de um dos lados do hexagono em cm: "))

Area_Hexagono = ((Lado * Raio) / 2) * 6

print("A área do hexágono tem {:.2f} cm²".format(Area_Hexagono))