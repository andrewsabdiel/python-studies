Dias_Alugados = int(input('Quantos dias alugados? '))
Km_Rodados = float(input('Quantos Km rodados? '))
Preço_dia = 60
Preço_Km = 0.15

Valor_Dias = Dias_Alugados * Preço_dia
Valor_Km = Km_Rodados * Preço_Km
Total_Pago = Valor_Dias + Valor_Km

print('O total a pagar é de R${:.2f}'.format(Total_Pago))
