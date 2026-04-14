# Exercício Gasolina
print("---- Olá! Irei lhe passar o valor do abastecimento! ----")

Comb = str(input("Insira G, para gasolina, ou A, para álcool: ")).upper()
Litr = float(input("Insira a quantidade em litros abastecidos: "))

print("-"*40)

Gasolina = "G"
Alcool = "A"

PG = 5.57 #Preço do litro da gasolina em R$
PA = 4.98 #Preço do litro do alcool em R$

Gat20 = 2 #Desconto para até 20 litros
Gac20 = 5 #Desconto para acima de 20 litros

Aat20 = 4 #Desconto para até 20 litros
Aac20 = 6 #Desconto para acima de 20 litros

# Calculos para Gasolina:

if Comb == Gasolina and Litr <= 20:
    Calculo1 = PG * Litr - ((Gat20 / 100) * (PG * Litr))
    print("Você deve pagar R${:.2f}".format(Calculo1))

elif Comb == Gasolina and Litr > 20:
    Calculo2 = PG * Litr - ((Gac20 / 100) * (PG * Litr))
    print("Você deve pagar R${:.2f}".format(Calculo2))

# Calculos para Alcool:

elif Comb == Alcool and Litr <= 20:
    Calculo3 = PA * Litr - ((Aat20 / 100) * (PA * Litr))
    print("Você deve pagar R${:.2f}".format(Calculo3))

elif Comb == Alcool and Litr > 20:
    Calculo4 = PA * Litr - ((Aac20 / 100) * (PA * Litr))
    print("Você deve pagar R${:.2f}".format(Calculo4))

print("-"*40)

print("Processo finalizado!")
print("Encerrando ...")

    
    
    

