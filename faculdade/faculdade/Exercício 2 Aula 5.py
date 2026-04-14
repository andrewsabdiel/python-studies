# Exercicio da imobiliaria
print("----- Olá! Iremos fazer o calculo do seu salário! -----")

Nome_Corretor = str(input("Insira o nome do corretor: "))
Qnt_Imove = int(input("Insira a quantidade de imóveis vendidos: "))
Val_Tot_Vend = float(input("Insira o valor total de suas vendas R$  "))

Salario = 1500 #Reais
Comissao = 200 #Reais
Comissao_por_venda = 5 #Por cento

Calculo = 1500 + (200 * Qnt_Imove) + ((5/100) * Val_Tot_Vend)

print("-"*40)
print("O salário final de {} é de R${:.2f}".format(Nome_Corretor, Calculo))
print("Processo Finalizado!")
print("Desligando...")
