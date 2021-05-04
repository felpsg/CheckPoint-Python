# Exercicio 1

horaAula = float(input("Digite seu valor hora-aula: "))
qtdAulas = int(input("Digite a quantidade de aulas semanas: "))
salarioBase = qtdAulas * 4.5 * horaAula
atividadeHora = salarioBase * 0.05
dsr = (salarioBase + atividadeHora) * (1 / 6)
salarioMensal = dsr + atividadeHora + salarioBase

print("Salário Base: ", salarioBase)
print("Atividade-hora: ", atividadeHora)
print("DSR: ", dsr)
print("Salário Mensal: ", salarioMensal)

