#-------------------------------------
# Diccionarios [Colección no ordenada de pares clave:valor]
#-------------------------------------

diccionario = {
    "nombre": "Gabriel Gonzalez",
    "Tecnologías": ["Python", "SQL"],
    "edad": 31,
    "Profession": "Estudiante",
    "ciudad": "Córdoba"
}


claves = diccionario.keys()
valores = diccionario.values()
items = diccionario.items() # Devuelve una Vista de tuplas de clave valor (clave, valor) ===> ("nombre", "Gabriel Gonzalez"), ... , podemos transformarla a lista con list(items)
lista_items = list(items)
nombre = diccionario["nombre"]

diccionario1 = diccionario.copy()

print(nombre)
print(claves)
print(valores)
print(items)
print(lista_items)
# lista2_items = dict(lista_items)
# print(lista2_items)
# print(type(lista2_items))

# Actualizar diccionario

diccionario.update({"nombre":"gabi gonz", "edad":30}) # Actualizo valores
diccionario.update({"hobbies":["Futbol","gaming"]}) # Sirve para actualizar y agregar items
print(diccionario)

diccionario.pop("Profession")
print(diccionario)

diccionario.popitem() # elimina el ultimo par clave valor del diccionario
print(diccionario)

del diccionario["nombre"]
print(diccionario)

diccionario.clear()
print(diccionario)

#del diccionario         Elimina el espacio de memoria de diccionario por lo que nos da error el print
#print(diccionario)

# copy
diccionario2 = dict(diccionario1)
diccionario4 = diccionario1 # No se debe hacer esto en estructuras de datos porque va a hacer referencia la mismo espacio en memoria, por lo que las modificaciones en uno se haran en los 2

print("\n")
print(diccionario1)
print("\n Recorrido con bucle for\n")
print("diccionario1 = {")
for key in diccionario1:
    print(f"\t{key.capitalize()}: {diccionario1[key]}")
print("}")

# desempaquetado de diccionario.items()

print("\n\n\n\n\n")
print("\n DESEMPAQUETANDO LOS ITEMS \n")
items = diccionario1.items()
print(items)
print("\n")
print("\n Recorrido con bucle for sobre items\n")
for key,value in items:
    print(f"{key.capitalize()} = {value} ----> Recorrido {key}")
