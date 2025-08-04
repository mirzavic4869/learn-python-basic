class Hero:  # template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("Sniper", 100, 10, 20)
hero2 = Hero("Mirana", 200, 20, 50)
hero3 = Hero("Sven", 400, 5, 30)

print(hero1.name)
print(hero2.__dict__)
print(hero3.armor)
