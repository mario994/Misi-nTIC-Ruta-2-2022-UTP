import pandas as pd

rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'


def listaPeliculas(rutaFileCsv: str) -> str:
    respuesta = ''
    #Comprueba si es un archivo csv valido
    if rutaFileCsv.find('.csv') != -1:
        try:
            df = pd.read_csv(rutaFileCsv)
            #Si hay un error al momento de leer el archivo tira una excepción
        except:
            respuesta = 'Error al leer el archivo de datos.'
        else:
            #pivot_table crea una tabla dinamica, esta función puede recibir multiples parametros 
            #filter() crea un subconjunto a partir de una tabla
            table = pd.pivot_table(df.filter(
                ['Country', 'Language', 'Gross Earnings']), index=['Country', 'Language'])
            respuesta = table.head(10)
    else:
        respuesta = 'Extensión inválida.'

    return respuesta


print(listaPeliculas(rutaFileCsv))
