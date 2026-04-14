pp = float(input('Qual o valor do produto? R$'))
Valor_Disconto = 5
Desconto = 5 / 100
Produto_Desconto = pp - (pp * Desconto)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(pp, Produto_Desconto))
