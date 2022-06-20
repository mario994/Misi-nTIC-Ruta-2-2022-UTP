def CDT(usuario:str, capital:int, tiempo:int):
    valorIntereses = 0
    valorTotal = 0
    
    if tiempo > 2:
        valorIntereses = capital * 0.03 * tiempo / 12
        valorTotal = valorIntereses + capital

        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario, capital, tiempo, valorTotal)

    else: 
        valorIntereses = capital * 0.02
        valorTotal = capital - valorIntereses

        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario, capital, tiempo, valorTotal)


print(CDT('user91', 1000000, 3))
print(CDT('user91', 650000, 2))
