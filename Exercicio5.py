# Exercicio 5

salario = float(input("Digite o seu salário: "))

if 1100 >= salario > 0:
    inss = salario * 0.075
elif salario <= 2203.48:
    inss = salario * 0.09
elif salario <= 3305.22:
    inss = salario * 0.12
elif salario <= 6433.57:
    inss = salario * 0.14

print("{:.2f}".format(inss))
