cedula = int(input("Digite o valor da cedula: "))
primeira = int(input("Digite o valor de uma moeda: "))
segunda = int(input("Digite o valor da outra moeda: "))

totalMoedaMenor, totalMoedaMaior = 0, 0

# Verifica qual o menor e qual o maior
menor = min(primeira, segunda)
maior = max(primeira, segunda)

# Verifica se existe resultado ou não
check = True
while (True):

    # Se em algum momento o numero for divisivel pelo maior numero
    # Entao divide por ele encerra
    # Se não vai subtraindo pelo menor numero
    if cedula % maior == 0:
        totalMoedaMaior = cedula / maior
        break
    else:
        totalMoedaMenor += 1
        cedula -= menor

    # Se for menor que o valor da menor moeda então
    # É pq nao existe resultado
    if cedula < menor:
        check = False
        break

if check == False:
    print("Nao e possivel fazer a troca")
else:
    # imprime
    if maior == primeira:
        print("Possivel: {} moeda(s) de {} e {} moeda(s) de {}".format(int(totalMoedaMaior), maior, totalMoedaMenor,
                                                                       menor))
    else:
        print("Possivel: {} moeda(s) de {} e {} moeda(s) de {}".format(totalMoedaMenor, menor, int(totalMoedaMaior),
                                                                       maior))