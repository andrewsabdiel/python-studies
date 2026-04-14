tipo = input("Qual o tipo de triangulo? ")
base = int(input("Insira o tamanho da base em centímetros"))
altura = int(input("Insira o valor da altura em centímetros"))

area = base * altura / 2

print("O triangulo é do tipo %s, sua base tem medida de %d cm, sua altura é de %d cm e área de %.2f cm²." % (tipo,base,altura,area))
