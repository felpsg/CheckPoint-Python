# Exercicio 3

consumoMensal = float(input("Digite seu consumo mensal em kWh: "))

if 50 >= consumoMensal > 0:
    valorConsumo = 14
else:
    valorConsumo = 14 + consumoMensal * 0.25

if 99 >= consumoMensal > 0:
    icms = 0
elif consumoMensal <= 200:
    icms = 0.13 * valorConsumo
else:
    icms = 0.33 * valorConsumo

valorTotal = icms + valorConsumo

print("Valor do Consumo: {:.2f}".format(valorConsumo))
print("Valor ICMS: {:.2f}".format(icms))
print("Valor total da conta: {:.2f}".format(valorTotal))

