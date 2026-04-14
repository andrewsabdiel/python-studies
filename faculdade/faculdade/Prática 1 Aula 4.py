from math import pow
x = float(input("Insira um primeiro valor: "))
y = float(input("Insira um segundo valor: "))

z = (pow(x,2) + pow(y,2))/(x + y)

print("O valor final de sua equação é {:.2f}".format(z))


