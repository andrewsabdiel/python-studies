# Exercício relação de tensão
print("---- Olá! Iremos checar a relação da tensão! ----")

# V = Tensão (volts)
# I = Corrente (amperes)
# R = Resistência (ohms)

V = float(input("Insira o valor da tensão (V) em volts: "))
I = float(input("Insira o valor da corrente (I) em amperes: "))
R = float(input("Insira o valor da resistência (R) em ohms: "))

print("-"*40)

# Calculo

V_real = I * R

if V_real == V:
    print("O componente obedece à Lei de Ohm.")

else:
    print("O componente não obedece à Lei de Ohm.")

print("-"*40)

print("Processo finalizado!")
print("Encerrando ...")
