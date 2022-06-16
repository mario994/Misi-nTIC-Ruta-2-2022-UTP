def ordenes(rutinaContable):
    numeroFactura = list(map(lambda num: num[0], rutinaContable))
    totalxRegistro = list(map(totalCompra, rutinaContable))
    resultado = "------------------------ Inicio Registro diario ---------------------------------\n"

    for elemento in zip(numeroFactura, totalxRegistro):
        resultado += "La factura {} tiene un total en pesos de {:,.2f}\n".format(
            elemento[0], round(elemento[1], 2))
            #El :, Hace que el numero aparesca con las comas de separación de centenas
            #El .2f "FUERZA" a que aparescan 2 digitos despues del punto decimal

    resultado += "-------------------------- Fin Registro diario ----------------------------------"

    return print(resultado)


def totalCompra(lista):
    totalSuma = 0

    for x in range(1, len(lista)):
        totalSuma += lista[x][1] * lista[x][2]

    if totalSuma < 600000:
        totalSuma += 25000

    return totalSuma

ordenes([
    [1201, ("5464", 4, 25842.99), ("7854", 18, 23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58), ("1112", 18, 2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20),
     ("1254", 1, 13645.20), ("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)]
])

ordenes([
    [6587, ("3268", 4, 25842.99), ("8274", 18, 23254.99),
     ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
    [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)]
])

ordenes([
    [6589, ("9874", 1, 125698.20), ("88112", 2,
                                    135645.20), ("3218", 4, 13645.20)],
    [6590, ("5236", 8, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)],
    [6591, ("7812", 2, 11.99), ("9652", 11, 18.99)],
])
