# Exercício de horas trabalhadas

valor = float(input("Insira o quanto você ganha por hora em R$: "))
horas = float(input("Insira a quantidade de horas tralhadas no mês: "))
print()

# valores
salario = valor * horas
imp_renda = 11 # Valor em %
INSS = 8 # Valor em %
sindicato = 5 # Valor em %

# valores pagos
imp_renda2 = salario * (imp_renda/100)
INSS2 = salario * (INSS/100)
sindicato2 = salario * (sindicato/100)
salario_liquido = salario - imp_renda2 - INSS2 - sindicato2

#Impressão de valores
print(f"Salário Bruto: R${salario:.2f}")
print(f" - Imposto de Renda ({imp_renda}%): R${imp_renda2:.2f}")
print(f" - INSS ({INSS}%): R${INSS2:.2f}")
print(f" - Sindicato ({sindicato}%): R${sindicato2:.2f}")
print(f"Salário liquido: R${salario_liquido:.2f}")
