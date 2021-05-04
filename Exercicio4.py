# Exercicio 4

mediaConsumoPassado = float(input("Digite a média de consumo em m³ ano  anterior: "))
mediaConsumoAtual = float(input("Digite o consumo em m³ do mês vigente: "))

if 20 > mediaConsumoAtual > 0:
    valorConsumo = mediaConsumoAtual * 2
elif 35 >= mediaConsumoAtual:
    valorConsumo = mediaConsumoAtual * 3.5
elif 50 >= mediaConsumoAtual:
    valorConsumo = mediaConsumoAtual * 5.5
else:
    valorConsumo = mediaConsumoAtual * 7

print("Valor do Consumo: ", valorConsumo)

if mediaConsumoAtual > (1.1 * mediaConsumoPassado):
    multaDesconto = 0.3 * valorConsumo
    print("Multa: ", multaDesconto)
else:
    multaDesconto = 0.2 * (-valorConsumo)
    print("Desconto: ", -multaDesconto)

valorTotal = valorConsumo + multaDesconto

print("Valor Total: ", valorTotal)

