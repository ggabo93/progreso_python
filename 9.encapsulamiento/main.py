from clases.cuenta_bancaria import CuentaBancaria

# Creación de objeto 
cuenta1 = CuentaBancaria("Gabriel Gonzalez", 1000)
print(cuenta1)

# Seteando datos de la cuenta mediante método setter

cuenta1.depositar(4000)
cuenta1.retirar(2400)

# Muestra de informacion mediante método getter
print(cuenta1.get_saldo())