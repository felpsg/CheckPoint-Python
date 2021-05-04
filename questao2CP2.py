# Recebe a quantidade de produtos
n = int(input("Digite a quantidade de produtos: "))

maiorPorcentagem, maiorValorEmR = 0.0, 0.0
for _ in range(n):
    # Recebe os valores dos preços dos produtos
    precoAtual = float(input("Digite o preco atual: "))
    precoAjustado = float(input("Digite o preco ajustado: "))

    # Se a diferença dos preços for maior que o preço guardado
    # Então recebe essa diferença
    if maiorValorEmR < precoAjustado - precoAtual:
        maiorValorEmR = precoAjustado - precoAtual

    # Faz uma regra de 3 e gera a porcentagem
    # Subtrai por - 100 para saber quantos % excedeu
    if maiorPorcentagem < ((precoAjustado / precoAtual) * 100) - 100:
        maiorPorcentagem = ((precoAjustado / precoAtual) * 100) - 100

print("O maior valor em R$ foi: {}".format(maiorValorEmR))
print("A maior porcentagem foi: {}".format(maiorPorcentagem))