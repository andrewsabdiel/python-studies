Preco_Or = float(input("Insira o preço original do produto: R$ "))
Valor_Desc = float(input("Insira quanto de desconto será dado em %: "))

Dscnt_Prcntgm = Valor_Desc / 100
Valor_Dscntd = Preco_Or * Dscnt_Prcntgm
Prc_c_Dscnt = Preco_Or - Valor_Dscntd

print("O valor original do produto é de R${:.2f}".format(Preco_Or))
print("O desconto dado foi de R${:.2f}".format(Valor_Dscntd))
print("O valor do produto com desconto é de R${:.2f}".format(Prc_c_Dscnt))
