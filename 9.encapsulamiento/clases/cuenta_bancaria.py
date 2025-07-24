class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial

    # Setter 
    def depositar(self, cantidad):
        if cantidad > 0 :
            self.__saldo += cantidad
            print(f"Deposito correcto. Nuevo saldo: ${self.__saldo}")
        else:
            print("Debe ingresar un monto mayor a 0")
    
    def retirar(self, cantidad):
        if 0 < cantidad < self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado ${cantidad} correctamente.")
        else:
            print("Seleccione una cantidad permitida. ")

    def get_saldo(self):
        return f"Saldo disponible: ${self.__saldo}"
    
    def __str__(self):
        return f"Cuenta: [{self.__titular}  -  Saldo disponible: ${self.__saldo}]"