# Exercicio 2

anosUso = int(input("Digite a quantidade de anos de vida/uso: "))
mesesUso = int(input("Digite a quantidade de meses de vida/uso: "))

mesesAntesDepois = int(input("Digite a quantidade de meses, utilizando numeros negativos para descobrir a "
                             "idade anterior a estes meses e positivos para descobrir qual idade terá "
                             "após tantos meses: "))

if mesesAntesDepois + mesesUso < 0:
    anosPorMes = int(((mesesAntesDepois + mesesUso) / 12 + anosUso))
    print("Idade em anos: ", anosPorMes)
else:
    anosPorMes = int((mesesAntesDepois + mesesUso) / 12)
    print("Idade em anos: ", anosPorMes + anosUso)

mesesPorMes = int((mesesAntesDepois + mesesUso) % 12)

print("Idade em meses: ", mesesPorMes)

