# --------------------
# SET  (conjunto)  Coleccion no ordenada (no tenemos indice para recorrer el set) y mutable
# --------------------

set_frutas = {"Manzana", "Kiwi", "Pera", "Limon"}
set_frutas1 = {"Fresa", "Melon", "Coco"}
set_frutas2 = set(("Naranja",))
lista_frutas = list(("Papaya", "Pomelo", 3, 5, False)) 

print(set_frutas2)
# Recorriendo el conjunto
for fruta in set_frutas:
    print(fruta)

# add
print("\nadd\n")
set_frutas.add("Mandarina")
print(set_frutas)

# remove
# set_frutas.remove("Manzana")
# print(set_frutas)

# in
print("\nin\n")
print("Kiwi" in set_frutas)
print("Kiwi" in set_frutas1)

# concatenar
print("\nconcatenar\n")
set_frutas.update(set_frutas1,set_frutas2,lista_frutas) # Se puede updatear con otras estructuras como lista.
print(set_frutas)
print(len(set_frutas))

# union
print("\nunion\n")
conjunto_letras = {"a","b","c"}
conjunto_numeros = {1,2,3}
tupla_numeros = (3,4,5)

union = conjunto_letras.union(conjunto_numeros)
union2 = conjunto_letras | conjunto_numeros

print(union)
print(union2)

# update
print("\nupdate\n")
conjunto_letras.update(tupla_numeros)
print(conjunto_letras)

# intersection
print("\nIntersection\n")
set_chicago = {"Python","JavaScript","AWS"}
set_oxford = {"Python","TypeScript","GoogleCloud"}
set3 = set_chicago - set_oxford # shorthand de set_chicago.diference(set_oxford)
print(set_chicago.intersection(set_oxford))
print(set_oxford.difference(set_chicago)) # Devuelve un set con los elementos que no estan en chicago
print(set3)