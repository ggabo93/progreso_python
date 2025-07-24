# Importamos de la carpeta clases, el archivo perro y la clase Perro

from clases.perro import Perro

# Creando un objeto tipo Perro
perro1 = Perro("Firu", 3)

# Impresion de variables y metodos del objeto
print(f"{perro1.nombre} de {perro1.edad} años, hace {perro1.ladrar()}.")
