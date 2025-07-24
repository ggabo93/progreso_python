texto = "hoLa muNdo"
texto_con_espacios = "    texto con espacios   "
texto_separado = "Python,JavaScript,Django,React"
lista = ["Hola","Juan","Carlos"]
numeros = "15646 51"
repeticion = "manzana, naranja, manzana, limon"
print("Texto: ", texto)
print("capitalize: ", texto.capitalize())
print("upper: ", texto.upper())
print("lower: ", texto.lower())
print("strip: ", texto_con_espacios.strip()) # elimina los espacios al principio y al final
print("replace: ", texto_con_espacios.replace("espacios", "gracias")) # cambia una palabra por otra
print("split: ", texto_separado.split(",")) # separar texto en items de una lista
print("join: ", ",".join(lista)) # junta items de una lista en un string
print("find: ", texto.find("muNdo")) # muesta la posicion donde comienza el texto ingresado
print("startswith: ", texto.startswith("hoLa"))
print("endswith: ", texto.endswith("muNdo"))
print("isdigit: ", numeros.isdigit()) # indica si todos los caracteres son numeros (los espacios no son numeros ni letras)
print("count: ",repeticion.count("manzana")) # indica cuantas veces aparece manzana
