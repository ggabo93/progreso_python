# ---------------------
# COPIAR Y JUNTAR LISTAS
# ---------------------

frutas1 = ["Manzana","Pera","Banana"]
frutas2 = ["Mandarina","Fresa"]

# METODOS PARA COPIAR LISTAS
frutas1_copia = frutas1.copy()
print(frutas1_copia)

frutas2_copia = list(frutas2)
print(frutas2_copia)

# CONCATENAR LISTAS
frutas = frutas1 + frutas2
print(frutas)

frutas1.extend(frutas2)
print("Frutas1 extendida: ",frutas1)