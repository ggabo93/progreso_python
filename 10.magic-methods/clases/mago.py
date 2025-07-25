class Mago():
    # __init__ es un magic method
    def __init__(self, nombre, hechizos):
        self.nombre = nombre
        self.hechizos = hechizos if hechizos else []
    
    # __str__ metodo toString
    def __str__(self):
        return f"Mi nombre es {self.nombre} y mis poderes son: {self.hechizos}"
    
    # __len__ devuelve el tamaño de algún atributo que querramos
    def __len__(self):
        return len(self.hechizos)
    
    # __eq__ compara si dos instancias son iguales
    def __eq__(self,otro):
        return self.nombre == otro.nombre and self.hechizos == otro.hechizos