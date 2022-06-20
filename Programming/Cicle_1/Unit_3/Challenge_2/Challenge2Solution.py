def cliente (informacion:dict) -> dict:
    resultado = {
        "nombre": informacion["nombre"],
        "edad": informacion["edad"],
        "atraccion": "",
        "apto": "",
        "primer_ingreso": "",
        "total_boleta": ""
    }

    if informacion["edad"] >= 7 and informacion["edad"] < 15:
        resultado["atraccion"] = "Sillas voladoras"
        resultado["apto"] = True
        resultado["total_boleta"] = 10000

        if informacion["primer_ingreso"]:
            resultado["primer_ingreso"] = True
            resultado["total_boleta"] = resultado["total_boleta"] - resultado["total_boleta"] * 0.05
        else:
            resultado["primer_ingreso"] = False
        
        return resultado

    elif informacion["edad"] >= 15 and informacion["edad"] <= 18:
        resultado["atraccion"] = "Carros chocones"
        resultado["apto"] = True
        resultado["total_boleta"] = 5000

        if informacion["primer_ingreso"]:
            resultado["primer_ingreso"] = True
            resultado["total_boleta"] = resultado["total_boleta"] - resultado["total_boleta"] * 0.07
        else:
            resultado["primer_ingreso"] = False
        
        return resultado

    elif informacion["edad"] > 18:
        resultado["atraccion"] = "X-Treme"
        resultado["apto"] = True
        resultado["total_boleta"] = 20000

        if informacion["primer_ingreso"]:
            resultado["primer_ingreso"] = True
            resultado["total_boleta"] = resultado["total_boleta"] - resultado["total_boleta"] * 0.05
        else:
            resultado["primer_ingreso"] = False
        
        return resultado

    else:
        resultado["atraccion"] = "N/A"
        resultado["apto"] = False
        resultado["primer_ingreso"] = True
        resultado["total_boleta"] = "N/A"
        
        return resultado


print (cliente({"Id_cliente": 1, "nombre": "Johana Fernandez", "edad":20, "primer_ingreso": True}))

print (cliente({"Id_cliente": 1, "nombre": "Johana Fernandez", "edad":20, "primer_ingreso": False}))

print (cliente({"Id_cliente": 2, "nombre": "Gloria Suarez", "edad":3, "primer_ingreso": True}))

print (cliente({"Id_cliente": 3, "nombre": "Tatiana Suarez", "edad":17, "primer_ingreso": True}))

print (cliente({"Id_cliente": 3, "nombre": "Tatiana Suarez", "edad":17, "primer_ingreso": False}))

print (cliente({"Id_cliente": 4, "nombre": "Tatiana Ruiz", "edad":8, "primer_ingreso": True}))

print (cliente({"Id_cliente": 4, "nombre": "Tatiana Ruiz", "edad":8, "primer_ingreso": False}))
    

