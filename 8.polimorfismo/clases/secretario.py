from clases.empleado import Empleado


class Secretario(Empleado):
    def __init__(self, nombre, sueldo,departamento,categoria):
        super().__init__(nombre, sueldo)
        self.departamento = departamento
        self.categoria = categoria

    def __str__(self):
        return f"{super().__str__()} - [Departamento: {self.departamento} - Categoria: {self.categoria}]"
