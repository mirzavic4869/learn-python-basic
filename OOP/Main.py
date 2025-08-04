class Hero:  # template
    pass


hero1 = Hero()  # object / instance
hero2 = Hero()
hero3 = Hero()

hero1.name = 'Sniper'
hero1.health = 100

hero2.name = 'Sven'
hero2.health = 300

hero3.name = 'Mirana'
hero3.health = 500

print(hero1.__dict__)
