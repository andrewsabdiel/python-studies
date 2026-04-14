# Exercício de cálculo de salário
print("---- Olá! Hoje iremos calcular seu novo salário! ----")

Sal = float(input("Insira o seu salário atual em R$: "))

V_Bas = 1000 # Valor que serve de base para o cálculo do novoi salário

print("-" * 40)

if Sal <= V_Bas:
    Aum1 = 10 # Valor do aumento em porcentagem
    Calc1 = Sal + (Sal * (Aum1 / 100))
    print("O seu novo salário será no valor de R${:.2f}".format(Calc1))

else:
    Aum2 = 5 # Valor do aumento em porcemntagem
    Calc2 = Sal + (Sal * (Aum2 / 100))
    print("O seu novo salário será no valor de R${:.2f}".format(Calc2))

print("-" * 40)

print("Processo finalizado!")
print("Encerrando ...")
    
        

