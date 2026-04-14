Preco_Or = float(input("Insira o valor original do produto: R$ "))
Desconto = 20
Preco_Dscntd = Preco_Or * (Desconto / 100)
Preco_c_Desc = Preco_Or - Preco_Dscntd

print("Preço original: R$ {:.2f}".format(Preco_Or))
print("Valor descontado: R$ {:.2f}".format(Preco_Dscntd))
print("Valor do produto com desconto: R$ {:.2f}".format(Preco_c_Desc))