# Exercício calculo de multa

limite = 50 # Valor em Kg
multa = 4.00 # Valor em R$

print(f"Peso limite: {limite}Kg")
print(f"Multa a ser paga por Kg: R${multa}")
print()

peso_peixes = float(input("Insira o peso de peixes em Kg: "))
print()

if peso_peixes > limite:

    excesso = peso_peixes - limite
    multa_paga = multa * excesso

    print(f"Você excedeu em {excesso:.2f} Kg o limite.")
    print(f"Você deve pagar R${multa_paga:.2f} de multa.")

else:

    print("O limite não foi ultrapassado.")
    print("Você não pagará multa.")

    
