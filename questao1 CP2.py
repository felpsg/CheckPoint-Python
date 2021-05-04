# Pega as entradas da questao
n = int(input("Digite o valor de n: "))
sequencia = list(map(int, input("Digite a lista dos valores: ").split()))

# Recebe o primeiro para comparar com os outros
atual = sequencia[0]
resposta = 1

# For iniciando do 1 para comparar com o primeiro
for i in range(1, n):
    # Se for diferente entao atribui 1 e recebe o novo valor
    # Se for igual nao faz nada
    if sequencia[i] != atual:
        resposta += 1
        atual = sequencia[i]

print(resposta)