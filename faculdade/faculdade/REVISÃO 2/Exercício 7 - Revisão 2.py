# Exercício de conversão de números
nume = float(input("Insira um número decimal: "))

print("Números decimais não podem ser convertidos.")
print("Por isso, convertemos apenas a parte inteira.")

nume_int = int(nume)

print(f"Inteiro: {nume_int}")
print(f"Hexadecimal = {hex(nume_int)}")
print(f"Binário = {bin(nume_int)}")
print(f"Octal = {oct(nume_int)}")
