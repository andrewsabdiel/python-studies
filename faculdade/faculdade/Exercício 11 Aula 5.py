# Exercício cálculo de torque
print("---- Olá! Iremos checar o torque do seu parafuso! ----")

#Torque aplicado:
T_Apl = float(input("Insira  o valor do torque aplicado (em Nm): "))

#Torque de aperto:
T_Apt = float(input("Insira o valor do torque de aperto recomendado (em Nm) para o parafuso: "))

VAbM = T_Apt - ((10/100) * T_Apt) # Valor minimo recomendado
VAcM = T_Apt + ((10/100) * T_Apt) # Valor máximo recomendado

print("-"*40)

if T_Apl >= VAbM and T_Apl <= VAcM:
    print("O parafuso está apertado corretamente.")

else:
    print("O parafuso não está apertado corretamente.")

print("-"*40)

print("Processo finalizado!")
print("Encerrando ...")

