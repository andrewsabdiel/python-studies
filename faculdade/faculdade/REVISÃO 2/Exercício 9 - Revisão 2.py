# Exercício de cálculo de salário

valor = float(input("Insira o quanto você ganha por hora em R$: "))
hora = float(input("Insira a quantidade de horas trabalhadas no mês: "))

valor_final = valor * hora

print("Nesse mês você irá receber R${:.2f}".format(valor_final))
