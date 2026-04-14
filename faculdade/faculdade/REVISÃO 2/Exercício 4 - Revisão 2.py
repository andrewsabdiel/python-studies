# Exercício de troca de variaveis

Valor1 = int(input("Insira o primeiro valor: "))
Valor2 = int(input("Insira o segundo valor: "))

print(f"O primeiro valor inserido foi {Valor1}")
print(f"O segundo valor inserido foi {Valor2}")

Valor1, Valor2 = Valor2, Valor1

print(f"O primeiro valor inserido foi trocado para {Valor1}")
print(f"O segundo valor inserido foi trocado para {Valor2}")
