### FUNCIONES LAMBDA

# Funcion para d uplicar un numero mediante
def duplicar(n):
    return n * 2

# Duplicar un numero mediante funcion lambda 
duplicar_lambda = lambda num: num * 2

print("DEF: ", duplicar(5))
print("LAMBDA: ", duplicar_lambda(5))

# Funcion multiplicar a,b
def multiplicar(a,b):
    return a*b

# Multiplicacion de dos numeros (a,b) mediante funcion lambda
multiplicar_lambda = lambda a,b: a*b

print("DEF: ", multiplicar(5,4))
print("LAMBDA: ", multiplicar_lambda(5,5))

# Cuadrado lambda

cuadrado_lambda = lambda n: n ** 2

print("Cuadrado lambda: ", cuadrado_lambda(8))



# lambda dentro de una funcion

# Operaciones
print("OPERACIONES LAMBDA \n")
def operaciones(operacion):
    if operacion == "suma":
        return lambda a,b: a+b
    elif operacion == "resta":
        return lambda a,b: a-b
    elif operacion == "multiplicacion":
        return lambda a,b: a*b
    else:
        return lambda a,b: a/b
    
suma = operaciones("suma")
resta = operaciones("resta")
multiplicacion = operaciones("multiplicacion")
division = operaciones("division")
print("Suma: ", suma(4,1))
print("Resta: ", resta(4,1))
print("Multiplicacion: ", multiplicacion(4,1))
print("Division: ", division(6,4))

# ORDENAR LISTA DE DICCIONARIOS CON LAMBDA

estudiantes = [
    {"nombre":"Juan", "edad": 20},
    {"nombre":"Maria", "edad": 25},
    {"nombre":"Pedro", "edad": 21}
]

estudiantes_ordenados = sorted(estudiantes, key = lambda x:x["edad"])
print("Estudiantes ordenados: \n", estudiantes_ordenados)