# Exercício 1 - Revisão Python
print("---- Olá! Hoje iremos fazer o cálculo de uma divisão! ----")

Nume = float(input(" Insira o valor do numerador: "))
Deno = float(input(" Insira o valor do denominador: "))

print("-" * 40)

if Deno == 0:
    print("Não é possivel fazer a divisão!")

else:
    Div = Nume/Deno
    print("O resultado da divisão é {:.2f}".format(Div))

print("-" * 40)
print("Processo finalizado!")
print("Encerrando ...")
    
