from math import pow
Altura = float(input("Insira a altura do paciente em metros: "))
Peso = float(input("Insira o peso do paciente em Kg: "))

IMC = Peso / pow(Altura, 2)

print("O Indice de Massa Corporal do Paciente é de {:.6f} Kg/m" .format(IMC))

