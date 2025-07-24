from clases.empleado import Empleado
from clases.gerente import Gerente
from clases.secretario import Secretario

def mostrar_detalles(empleado):
    print(empleado)

empleado = Empleado("Gabriel", 3100)
gerente = Gerente("Sofia", 6000, "Calidad",1)
secretario = Secretario("Lourdes", 2500, "Administración",3)

mostrar_detalles(empleado)
mostrar_detalles(gerente)
mostrar_detalles(secretario)
