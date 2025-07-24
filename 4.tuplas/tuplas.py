# ---------------------------------------
#    TUPLAS [Colección inmutable y ordenado]
# ---------------------------------------

frutas = ("Manzana","Pera","Banana","Kiwi")
print(frutas)
print(type(frutas))

# Creacion de tupla mediante constructor
frutas = tuple(("Manzana",))
print(frutas)
print(type(frutas))

# Actualizacion de tuplas

frutas = ("Manzana","Pera","Banana","Kiwi")

# Cambiar un elemento de la tupla

frutas2 = list(frutas) # Obtenemos una lista con los elementos de la tupla frutas

frutas2[1] = "Coco" # Reemplazamos el valor del elemento

frutas = tuple(frutas2) # Casteamos la lista frutas2 a tupla y la asignamos a la tupla original frutas
print(frutas)

# Agregar un elemento a la tupla

tupla_frutas = ("Manzana","Pera","Banana","Kiwi")
lista_frutas = list(tupla_frutas) # Creamos una lista con los valores de la tupla
print(tupla_frutas)

lista_frutas.append("Coco") # Realizamos la modificacion sobre la lista
tupla_frutas = tuple(lista_frutas) # Casteamos la lista_frutas a tupla y la asignamos a la variable original tupla_frutas
print(tupla_frutas)

# Concatenar tuplas

tupla_verduleria = ("Manzana","Pera","Banana","Kiwi")
tupla_verduras = ("Ajo","Tomate","Perejil")

tupla_verduleria += tupla_verduras
print(tupla_verduleria)

# Eliminar elemento

tupla_frutas = ("Manzana","Pera","Banana","Kiwi")
lista_frutas = list(tupla_frutas)

lista_frutas.remove("Manzana")
tupla_frutas = tuple(lista_frutas)
print(tupla_frutas)
print(type(tupla_frutas))

# Ejercicio para modificar una tupla mediante comprehension list

tupla = tuple(tupla_verduleria)
lista = list(tupla)

lista_sin_e = [producto for producto in lista if "e" not in producto] # Obtengo una lista donde los productos no contienen la letra e
tupla = tuple(lista_sin_e) # Casteamos la lista a tupla y la asignamos a la tupla original
print(tupla)

# Ordenar una tupla

lista.sort(key= str.lower)
tupla = tuple(lista)
print(tupla)

# Mostrar tupla con bucles

print(tupla_verduleria)

for verdura in tupla_verduleria:
    print(verdura)

for i in range(len(tupla_verduleria)):
    print(f"{i+1}. {tupla_verduleria[i]}")

i = 0
print("\nImprimiendo con while\n")
while i < len(tupla_verduleria):
    print(tupla_verduleria[i])
    i += 1

