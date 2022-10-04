class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_depósito(self, amount):
    	self.balance_cuenta += amount
        return self

    def hacer_retiro(self, amount):	
    	self.balance_cuenta -= amount
        return self

    def transfer_dinero(self, other_user, amount):
        self.balance_cuenta -=amount
        other_user.balance_cuenta +=amount
        return self

    def mostrar_balance_usuario(self):
        print(self.name)
        print(self.balance_cuenta)
        return self

guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
siegmund = Usuario("Siegmund Marggraf", "siegmund@python.com")

guido.hacer_depósito(300).hacer_depósito(500).hacer_depósito(200).hacer_retiro(400)
guido.mostrar_balance_usuario()
monty.hacer_depósito(1000)
monty.mostrar_balance_usuario()
siegmund.hacer_depósito(5000).hacer_retiro(500).hacer_retiro(150).hacer_retiro(600)
siegmund.mostrar_balance_usuario()
monty.transfer_dinero(siegmund, 500)
monty.mostrar_balance_usuario()
siegmund.mostrar_balance_usuario()