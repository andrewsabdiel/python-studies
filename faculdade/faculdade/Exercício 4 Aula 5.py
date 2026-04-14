# Exercício Hierarquia de números
print("---- Olá! Iremos ver qual dos dois números é maior! ----")

V1 = int(input("Insira o primeiro número: "))
V2 = int(input("Insira o segundo número: "))

print("-"*40)

if V1 > V2:
    print("O número {} é maior que o número {}.".format(V1, V2))

elif V1 == V2:
    print("O número {} é igual ao número {}.".format(V1, V2))

else:
    print("O número {} é menor que o número {}.".format(V1, V2))

print("-"*40)
print("Processo finalizado!")
print("Encerrando...")
