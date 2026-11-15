def greet(nome, ultimo_nome):
    print(f'oi {nome} {ultimo_nome}')

greet(nome='Jhonata', ultimo_nome='lixo')
greet(nome='Monica', ultimo_nome='lixo')
greet(nome='Alex', ultimo_nome='lixo')
greet(nome='Jhon Lennon', ultimo_nome='lixo')

disconto = 20

def calculo_de_preco(preco, disconto):
    promo = 0.8
    disconto = 10  # variável local, só existe dentro da função

    # cálculo
    taxa = promo * disconto          # 0.8 * 10 = 8.0
    preco_final = preco + taxa - disconto  # 100 + 8 - 10 = 98.0

    # printa o preço final
    print(f'total: ${preco_final}')

calculo_de_preco(preco=100)