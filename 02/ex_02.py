def obter_lucro_maximo(precos: list[float]) -> float:

    melhor_dia_compra = []
    melhor_dia_venda = []

    menor_preco = 0
    maior_preco = 0

    for m in precos:
        menor_preco -= m
        # if menor_preco < m:
        melhor_dia_compra.append(menor_preco)

        # if maior_preco > m:
        maior_preco += m
        melhor_dia_venda.append(maior_preco)

    return melhor_dia_compra - melhor_dia_venda

# def obter_lucro_maximo_sem_lucro(precos: list[float]) -> float:
#
#
