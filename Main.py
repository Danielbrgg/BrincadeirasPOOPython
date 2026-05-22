class Personagem:
    def __init__(self, nome, classe, vida, dano):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.dano = dano

    def atacar(self):
        print(f"{self.nome} atacou o alvo!")

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Vida: {self.vida}")
        print(f"Dano: {self.dano}")


class Mago(Personagem):
    def __init__(self, nome, classe, vida, dano, mana):

        super().__init__(nome, classe, vida, dano)

        self.mana = mana

    def mostrar_informacoes(self):

        super().mostrar_informacoes()

        print(f"Mana: {self.mana}")

    def lancar_magia(self):

        self.mana -= 40

        print(f"{self.nome} lançou uma magia!!")
        print(f"Mana restante: {self.mana}")

    def curar(self):

        self.mana -= 15
        self.vida += 20

        print(f"{self.nome} curou-se!")
        print(f"Vida atual: {self.vida} HP")
        print(f"Mana atual: {self.mana} MP")


class Guerreiro(Personagem):
    def __init__(self, nome, classe, vida, dano, armadura):

        super().__init__(nome, classe, vida, dano)

        self.armadura = armadura

    def mostrar_informacoes(self):

        super().mostrar_informacoes()

        print(f"Armadura: {self.armadura}")

    def defender(self):

        self.vida += self.armadura

        print(f"{self.nome} defendeu {self.armadura} de dano!")
        print(f"Vida atual: {self.vida} HP")


p1 = Guerreiro("Gael", "Guerreiro", 100, 20, 20)

p2 = Mago("Gandalf", "Mago", 80, 30, 100)

print("Primeiro Turno!!!\n")
print(f"Turno do {p2.classe}")
p2.mostrar_informacoes()

p2.atacar()
p2.lancar_magia()

print(f"Turno do {p2.classe} acabado!")

print(f"Turno do {p1.classe}")

p1.mostrar_informacoes()
p1.defender()
p1.atacar()
