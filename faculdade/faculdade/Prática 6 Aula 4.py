Dinheiro = float(input("Digite o valor que irá usar para abastecer: R$ "))
Preco_L = 4.95 # preço do litro
Autonomia = 20 # Km/L

Comb_Adq = Dinheiro / Preco_L
Dist_Adq = Autonomia * Comb_Adq

print("O veiculo foi abastecido com: {:.2f}L".format(Comb_Adq))
print("Autonomia: {:.2f} Km".format(Dist_Adq))
