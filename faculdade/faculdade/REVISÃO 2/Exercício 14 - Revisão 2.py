#Exercício de exibição do maior e menor número:

valor_1 = float(input("Insira o primeiro valor: "))
valor_2 = float(input("Insira o segundo valor: "))
valor_3 = float(input("Insira o terceiro valor: "))
print()

maior_valor = max(valor_1, valor_2, valor_3)
menor_valor = min(valor_1, valor_2, valor_3)

print(f"Dentre os valores, o maior é {maior_valor}")
print(f"Dentre os valores, o menor é {menor_valor}")
