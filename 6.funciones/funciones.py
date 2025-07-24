# #-----------------------------------
# # Funciones recursivas
# #-----------------------------------

def saludar():
    print("Hola mundo")

saludar()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(0))

def contador(n):
    print(n)
    n+=1
    if n < 10:
        contador(n)
contador(1)

# Suma los digitos de un numero 

def suma_digitos(n):
    if n % 10 == n:
        return n
    else:
        return n % 10 + suma_digitos(n//10)

print(suma_digitos(1234))

#Cuenta la cantidad de digitos que tiene un numero

def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n//10)

print(contar_digitos(1))

# Potencia

def potencia(a,b):
    if b == 0:
        return 1
    else:
        return a * potencia(a,b-1)

print(potencia(2,4))

##### LAMBDA


