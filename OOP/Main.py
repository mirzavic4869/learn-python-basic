class Hero:  # template
    # class variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat hero dengan nama " + inputName)


hero1 = Hero("Sniper", 100, 10, 20)
print(Hero.jumlah)
hero2 = Hero("Mirana", 200, 20, 50)
hero3 = Hero("Sven", 400, 5, 30)

print(Hero.jumlah)
