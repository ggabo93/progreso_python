#-------------------------------------
# Diccionarios anidados [Colección no ordenada de pares clave:valor]
#-------------------------------------

familia = {
    "padre" : {
        "nombre": "Raul",
        "posicion": "Carpintero",
        "tec": [1, 3, 4, 5]
    },
    "madre" : {
        "nombre": "Patricia",
        "posicion": "Abogada",
        "tec": [1, 3, 4, 5]
    },
    "hijo" : {
        "nombre": "Pedro",
        "posicion": "Desempleado",
        "tec" : [1, 3, 4, 5]
    }
}
#print(familia["padre"]["nombre"])


familia_items = familia.items()

for pariente, data in familia_items:
    print(pariente)
    for value in data:
        print(f"{value}: {data[value]}")