class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interés, balance): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        # tu código aquí (recuerda, los atributos de instancia van aquí)
        # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
    def depósito(self, amount):
        self.balance += amount
        return self
    def retiro(self, amount):
        self.balance -= amount
        return self
    def mostrar_info_cuenta(self):
        print("Usted posee un monto de", self.balance, "pesos")
        return self
    def generar_interés(self):
        self.balance = self.balance + (self.balance * self.tasa_interés)
        return self

class CuentaBancaria2:
    def __init__(self, tasa_interés, balance): 
        self.tasa_interés = tasa_interés
        self.balance = balance
    def depósito(self, amount):
        self.balance += amount
        return self
    def retiro(self, amount):
        self.balance -= amount
        return self
    def mostrar_info_cuenta(self):
        print("Usted posee un monto de", self.balance, "pesos")
        return self
    def generar_interés(self):
        self.balance = self.balance + (self.balance * self.tasa_interés)
        return self

class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interés = 0.02, balance = 0)
        self.cuenta2 = CuentaBancaria2(tasa_interés = 0.02, balance = 0)


Usuario1 = Usuario("Siegmund Marggraf", "siegmund@python.cl")
Usuario2 = Usuario("Iosif Uesara", "iosif@python.cl")

Usuario1.cuenta.mostrar_info_cuenta().depósito(50000).generar_interés().retiro(6000).mostrar_info_cuenta()
Usuario2.cuenta.mostrar_info_cuenta()
Usuario1.cuenta2.mostrar_info_cuenta().depósito(6000).mostrar_info_cuenta()