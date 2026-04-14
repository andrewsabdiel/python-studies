# Exercício de calculo e classificação de notas
print("---- Olá! Iremos calcular e classificar suas notas! ----")

Nota_1 = float(input("Insira a nota da sua primeira avaliação: "))
Nota_2 = float(input("Insira a nota da sua segunda avaliação: "))
Nota_3 = float(input("Insira a nota da sua terceira avaliação: "))

Media = (Nota_1 + Nota_2 + Nota_3) / 3

print("-"*40)

print("Sua média é {:.2f} pontos.".format(Media))

if Media >= 7.0:
    print("Parabéns! Sua média é alta.")

elif Media >= 5.0:
    print("Sua média é razoável.")

else:
    print("Sua média é baixa. É uma boa oportunidade para melhorar.")


print("-"*40)

print("Processo finalizado!")
print("Encerrando...")
