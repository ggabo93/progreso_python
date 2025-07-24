#-------------------------------
# Tipos de datos SECUENCIA / COLECCION
#-------------------------------

# -list (lista)
from enum import nonmember


mi_lista = [1,2,3,4,5]

# -tuple (tupla) # Estructura inmutable
mi_tupla = (1,2,3,4)

# -range (rango)
range = (0,10)

#-------------------------------
# Tipos de datos de mapeo (MAPPING TYPE)
#-------------------------------

diccionario = {
    "nombre": "Gabriel",
    "edad": 31,
    "tecnologias": ["Python", "SQL"] # LISTA COMO PARTE DEL VALOR DE LA CLAVE, DE UN DICCIONARIO
}

#-------------------------------
# Tipos de datos de conjunto (set)
#-------------------------------

# -set (conjunto) [Colección no ordenada y mutable de datos únicos
conjunto = {1,2,3,4}

#-------------------------------
# Tipo de dato NULO
#-------------------------------

# NoneType (nulo) [Representa la ausencia de valor o la no asignacion]
nulo = None
