import random
from collections.abc import Sequence

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto aluno: '))

sequence = [n1, n2, n3, n4]
random.shuffle(sequence)

print('A ordem de apresentação será:')
print(sequence)