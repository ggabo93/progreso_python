# ---------------------------------------
#    TUPLAS [Colección inmutable y ordenado] DESEMPAQUETADO1
# ---------------------------------------


# Se desempaqueta los componentes de la tupla en variables

frutas = ("Manzana","Pera","Banana","Kiwi","Fresa", "Mandarina")
frutas2 = ("Ajo","Tomate","Perejil")
frutas3 = frutas * 3 + frutas2
(a, b, *c) = frutas
print(a)
print(b)

# Count
print(frutas3)
print(frutas3.count("Manzana"))

