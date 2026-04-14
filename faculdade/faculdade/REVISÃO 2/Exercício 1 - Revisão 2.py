# Exerpicio de elaboração de scripts
print("---- Olá, hoje iremos fazer algumas atividades! ----")
print("-" * 40)

print("---- Exercício de duplicar ----")
numero = float(input("Insira qualquer número real: "))
calculo = numero * 2
print("O dobro de {} é {}".format(numero, calculo))
print( )
print( )


print("---- Exercício de calculo de área ----")
comprimento = float(input("Insira o comprimento em metros da sua sala: "))
largura = float(input("Insira a largura em metros da sua sala: "))

area = comprimento * largura

print("A área da sua sala é de {:.2f}m²".format(area))
print( )
print( )


print("---- Exercício de calculo de pagamento ----")
valor_compra = float(input("Insira o valor do produto: R$ "))
desconto = float(input("Insira a porcentagem de desconto: "))/100

calculo = valor_compra + (valor_compra * desconto)

print("O cliente irá pagar R${:.2f}".format(calculo))

