# ---------------------
# ORDENAMIENTO DE LISTAS
# ---------------------

frutas = ["Manzana","Pera","Banana","Mandarina","Fresa", "fresa","mandarina"] # EL ORDENAMIENTO ES CASE SENSITIVE, POR LO QUE LAS MINUSCULAS SE CONSIDERAN MAYORES QUE LAS MAYUSCULAS
frutas.reverse() # Devuelve la lista al reves
print(frutas)

frutas.sort()
print(frutas)

frutas.sort(key = str.lower) # Toma todo como si fuese minuscula y nos devuelve la lista ordenada sin importar si es mayuscula o minuscula
print(frutas)


numeros = [1, 4, 2, 10, 3, 0]
print(numeros)
numeros.sort(reverse=True)
print(numeros)