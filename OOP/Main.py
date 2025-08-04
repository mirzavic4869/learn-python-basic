class Hero:  # template
    # class variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

    # void function => method tanpa return, tanpa argumen
    def siapa(self):
        print("namaku adalah " + self.name)

    # method dengan argumen, tanpa return
    def healthUp(self, up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("Sniper", 100, 10, 20)
hero2 = Hero("Mirana", 200, 20, 50)
hero3 = Hero("Sven", 400, 5, 30)

hero2.siapa()
hero3.healthUp(20)

print(hero3.getHealth())
