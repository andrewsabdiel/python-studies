from math import sin, cos, tan, radians
Angl = float(input('Digite o ângulo que você deseja: '))
rad = radians(Angl)
sen = sin(rad)
cosen = cos(rad)
tang = tan(rad)

print('O ângulo de {} tem o SENO de {:.2f}'.format(Angl, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(Angl, cosen))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(Angl, tang))