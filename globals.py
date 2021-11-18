def main():
    
    alimentos = {
        'Bananas':10,
        'Laranjas':40,
        'Cenouras':35,
        'Uvas':12,
        'Arroz':60,
        'Feijao':23,
        'Macarrao':17
    }

    total_kg = calcula_total(alimentos)

    
    print(f'O total de alimentos disponíveis é: {total_kg} kg')

    calcula_porc(alimentos, total_kg)


def calcula_total(alimentos):
    # Calcula o total e retorna
    return sum(alimentos.values())


def calcula_porc(alimentos, total):
    for i in alimentos.items():
        nome_alimen = i[0]
        alimen_porc = round((i[1] * 100) / total, 2)
        salva_dados(nome_alimen, alimen_porc)


def salva_dados(nome_alimen, alimen_porc):
    arquivo = open('quantidade_alimentos.txt', 'a')
    arquivo.write(nome_alimen + ' - ' + str(alimen_porc) + '%' + '\n')
    arquivo.close()

if __name__ == '__main__':
    main()