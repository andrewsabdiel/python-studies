# Exercício de cálculo de velocidade
print("---- Olá! Hoje iremos checar sua velocida! ----")
print()

velo_maxima = float(input("Insira a velocidade máxima permitida em km/h: "))
velo_motorista = float(input("Insirá a velocida em que você estava em km/h: "))

print()
print()

if velo_motorista <= velo_maxima:
    
    print("O motorista não ultrapassou o limite de velocidade, portanto não levará multa.")
    

elif velo_motorista > velo_maxima and velo_motorista <= (velo_maxima + 10):
    multa = 85.13 # Valor em reais
    pontos = 3 # Pontos perdidos na carteira
    tipo = "leve" 

    print("O motorista receberá uma multa de tipo {}.".format(tipo))
    print("O motorista perderá {} pontos na carteira.".format(pontos))
    print("O motorista deverá pagar R${:.2f}".format(multa))


elif velo_motorista > (velo_maxima + 10) and velo_motorista <= (velo_maxima + 30):
    multa = 127.69 # Valor em reais
    pontos = 5 # Pontos perdidos na carteira
    tipo = "média" 

    print("O motorista receberá uma multa de tipo {}.".format(tipo))
    print("O motorista perderá {} pontos na carteira.".format(pontos))
    print("O motorista deverá pagar R${:.2f}".format(multa))

else:

    multa = 574.62 # Valor em reais
    pontos = 7 # Pontos perdidos na carteira
    tipo = "gravíssima" 

    print("O motorista receberá uma multa de tipo {}.".format(tipo))
    print("O motorista perderá {} pontos na carteira.".format(pontos))
    print("O motorista deverá pagar R${:.2f}".format(multa))


    
    
