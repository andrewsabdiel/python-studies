# Exercício de classificação de letras
print("---- Olá! Iremos classificar as letras de acordo com os gêneros! ----")

Letra = str(input("Digite uma letra do alfabeto: ")).upper()

Masculino = "M"
Feminino = "F"

print("-"*40)

if Letra == Feminino:
    print("A sua letra condiz com o gênero feminino.")

elif Letra == Masculino:
    print("A sua letra condiz com o gênero masculino.")

else:
    print("A sua letra não condiz com nenhum dos gêneros.")

print("-"*40)

print("Processo finalizado!")
print("Encerrando...")

