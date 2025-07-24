# ---------------------
# LISTAS
# ---------------------

lista = ["Manzana","Banana","Pera","Fresa","Mandarina"]

# Formas de mostrar elementos de una lista
print(lista[2])
print(lista[:3])
print(lista[2:])

# Verificar si un valor se encuentra en la lista
if "Banana" in lista:
    print("Si, Banana esta en la lista.\n")
print(lista)

# Agregar valores a la lista
lista[1] = "Platano"
lista[4] = "Toronja"
print(lista)

# Agregar valores a la lista mediante metodo insert
lista.insert(2,"Frutilla")
print(lista)

# Agrega valor a la lista en el ultimo indice
lista.append("Palta")
print(lista)

lista2 = ["Uva","Naranja","Manzana"]

# Extiende la lista a partir de otra lista
lista.extend(lista2)
print(lista)

# ---------------------------
# BUCLES PARA MANIPULAR LISTAS
# ---------------------------

for fruta in lista:
    print(fruta)

# shorthand (abreviacion)
print("\n   SHORTHAND\n")
[print(fruta) for fruta in lista]
print("\n   FINSHORTHAND\n")
for i in range(len(lista)):
    print(f"En en índice {i}, se encuentra la fruta: ", lista[i])

print("\n")
i = 0
while i < len(lista):
    print(f"WHILE. En en indice {i}, se encuentra la fruta: ",lista[i])
    i += 1