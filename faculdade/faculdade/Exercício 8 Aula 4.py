# Exercício de contagem de caracteres
frase = str(input("Digite uma frase: "))

f_cont = frase.lower()

contagem = frase.count('a')
print("-"*40)
print("A frase escrita é '{}'".format(frase))
print("-"*40)
print("O número de letras A que exixte na frase é {}".format(contagem))
