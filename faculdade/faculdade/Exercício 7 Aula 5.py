# Exercício de classificação de letras em vogais ou consoantes
print("---- Olá! Iremos classificar as letras em vogais ou consoantes! ----")

Letra = str(input("Digite uma letra do alfabeto: ")).upper()

Vogais = "A", "E", "I", "O", "U"

print("-"*40)

if Letra == Vogais:
    print("A letra digitada é uma vogal")

else:
    print("A letra digitada é uma consoante")

print("-"*40)

print("Processo finalizado!")
print("Encerrando...")
