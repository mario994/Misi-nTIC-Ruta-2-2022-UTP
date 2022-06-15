def AutoPartes(ventas):
    # Creamos un diccionario vacio
    diccionarioVentas = {}
    # Actualiza el diccionario con listas de tuplas
    for x in range(len(ventas)):
        diccionarioVentas[x] = [ventas[x]]

    return diccionarioVentas


def consultaRegistro(ventas, idProductos):
    datosEncontrados = {}

    # iteramos ventas, que es el retorno de la función AutoPartes
    for x in ventas:
        # Si hay coincidencia de valores se retorna la lista al nuevo diccionario
        if ventas[x][0][0] == idProductos:
            datosEncontrados[x] = ventas[x]

    # Si datosEncontrados tiene algún valor
    if datosEncontrados:
        # Creamos una variable de tipo string vacia
        respuesta = ""

        for x in datosEncontrados.values():
            # retornamos el string formateado a la variable respuesta
            respuesta += "Producto consultado : {}  Descripción  {}  #Parte  {}  Cantidad vendida  {}  Stock  {}  Comprador {}  Documento  {}  Fecha Venta  {}\n".format(
                x[0][0], x[0][1], x[0][2], x[0][3], x[0][4], x[0][5], x[0][6], x[0][7])
        return print(respuesta)

    else:
        return print("No hay registro de venta de ese producto")


consultaRegistro(AutoPartes([
    (9852, 'Culata', 'XC9875', 2, 165, 'Luis Molero', 3455846, '14/06/2020'),
    (9852, 'Culata', 'XC9875', 2, 165, 'Jose Mejia', 1355846, '14/06/2020'),
    (2564, 'Cárter', 'PT29872', 2, 32, 'Peter Cerezo', 8545436, '14/06/2020'),
    (5412, 'válvula', 'AZ8798', 2, 11, 'Juan Peña', 568975, '14/06/2020')]), 9852)
