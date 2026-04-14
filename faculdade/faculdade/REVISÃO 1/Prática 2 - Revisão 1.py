# Exercício de escolha de maior valor

print("---- Olá! Hoje iremos escolhar o maior dos valores. ----")

V1 = float(input("Insira o primeiro valor: "))
V2 = float(input("Insira o segundo valor: "))

print("-" * 40)

if V1 > V2:
    print("O número {} é maior que o número {}.".format(V1, V2))

elif V1 < V2:
    print("O número {} é maior que o número {}.".format(V2, V1))

else:
    print("Ambos os valores são iguais.")

print("-" * 40)

print("Processo finalizado!")
print("Encerrando ...")
