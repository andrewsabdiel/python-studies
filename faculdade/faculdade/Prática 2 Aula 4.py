v_m = float(input("Digite o quanto um objeto foi deslocado em metros: "))
t_s = float(input("Digite quanto tempo durou o deslocamento em segundos: "))

Velo_Media = v_m / t_s

print("O objeto percorreu {:.2f} metros em {:.2f} segundos com velocidade média de {:.2f} m/s".format(v_m, t_s, Velo_Media))
