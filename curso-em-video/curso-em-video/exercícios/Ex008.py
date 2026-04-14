d_m = float(input('Insira a distância em metros: '))
d_km = d_m / 1000
d_hm = d_m / 100
d_dam = d_m / 10
d_dm = d_m * 10
d_cm = d_m * 100
d_mm = d_m * 1000

print('A medida de {}m corresponde a:\n{} km\n{} hm\n{} dam\n{} dm\n{} cm\n{} mm'.format(d_m, d_km, d_hm, d_dam, d_dm, d_cm, d_mm))