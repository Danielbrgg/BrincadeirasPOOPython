class ContaBancaria: 
    def __init__(self,nome,saldo):
        self.nome = nome
        self.saldo = saldo
        
    def depositar(self,valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        print(f"Olá {self.nome}, seu saldo é de: R$ {self.saldo}")

c1 = ContaBancaria("Daniel", 17, 5000)

c1.depositar(300)

c1.sacar(2000)

c1.mostrar_saldo()

""""
class ContaPremium(ContaBancaria):
    def __init__(self, nome, saldo, limite):
        super().__init__(nome, saldo)

        self.limite = limite
"""
