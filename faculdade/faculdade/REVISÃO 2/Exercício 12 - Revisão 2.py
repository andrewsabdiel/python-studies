# Exercício de leitura de notas parciais

nota1 = float(input("Insirá o valor da primeira nota: "))
nota2 = float(input("Insirá o valor da degunda nota: "))
print()

media = 7 #Media que o aluno deve alcançar para passar
media_aluno = (nota1 + nota2)/2 #Media alcançada pelo aluno

if media_aluno >= media and media_aluno < 10:
    print("Aluno aprovado!")

elif media_aluno <media:
    print("Aluno reprovado!")

else:
    print("Aluno aprovado com Distinção!")




