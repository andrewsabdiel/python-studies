Salário_Ini = float(input('Qual é o salário do funcionário? R$'))
Aumento = 15
Por_Aumento = 15/100
Salário_Final = Salário_Ini + (Salário_Ini * Por_Aumento)

print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(Salário_Ini, Salário_Final))

