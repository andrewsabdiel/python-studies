L_Parede = float(input('Insira a largura da parede em metros: '))
At_Parede = float(input('Insira a altura da parede em metros: '))
Area_Parede = L_Parede * At_Parede
Volume_Tinta = Area_Parede / 2

print('Sua parede tem dimensão de {} X {} e sua área é de {}'.format(L_Parede, At_Parede, Area_Parede))
print('Para pintar essa parede, vocêr precisará de {} l de tinta'.format(Volume_Tinta))