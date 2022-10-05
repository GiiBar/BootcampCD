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

siegmund = CuentaBancaria(0.01, 5000)
iosif = CuentaBancaria2(0.01, 2500)

siegmund.depósito(1000).depósito(600).depósito(4500).retiro(4000).generar_interés().mostrar_info_cuenta()
iosif.depósito(20000).depósito(50000).retiro(1000).retiro(750).retiro(9000).retiro(500).generar_interés().mostrar_info_cuenta()