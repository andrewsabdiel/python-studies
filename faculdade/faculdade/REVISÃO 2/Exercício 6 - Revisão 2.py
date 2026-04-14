# Exercício para descoberta de ano bissexto

Ano = int(input("Digite um ano: "))

if (Ano % 4 == 0 and Ano % 100 != 0) or (Ano % 400 == 0):

    print("O ano é bissexto")

else:
    print("O ano não é bissexto")
