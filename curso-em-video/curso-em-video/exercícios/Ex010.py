Valor_Real = float(input('Quanto de dinheiro você tem na carteira? R$'))
Valor_Dolar = Valor_Real / 5.17

print('Com R${} você pode comprar US${:.2f}'.format(Valor_Real, Valor_Dolar))