# Exercício de alteração de frase
frase = str(input("Digite uma frase: "))

Maius = frase.upper()
S_Esp = frase.replace(" ", "")
Maiu_s_Esp = Maius.replace(" ", "")
print('-'*60)
print("Sua frase em maiusculo fica assim:")
print(" -- {} --".format(Maius))
print('-'*60)
print("Sua frase sem espaçamento ficca assim:")
print(" -- {} --".format(S_Esp))
print('-'*60)
print ("Sua frase em maiusculo e sem espaçamentos fica assim:")
print(" -- {} --".format(Maiu_s_Esp))
print('-'*60)

