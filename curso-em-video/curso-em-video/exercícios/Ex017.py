from math import pow
from math import sqrt
Cco = float(input('Comprimento do cateto oposto: '))
Cca = float(input('Comprimento do cateto adjacente: '))

Quad_Hip = (pow(Cco, 2)) + (pow(Cca, 2))
Raiz_Hip = sqrt(Quad_Hip)

print('A hipotenusa vai medir {:.2f}'.format(Raiz_Hip))

