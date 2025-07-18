
# class

class Unit:
    # __init__
    def __init__(self, name, hp): # ignore self parameter when you create instances of classes
        # these are member variabels
        self.name = name
        self.hp = hp

# create instances below
marine  = Unit("marine", 30)      # `self` parameter is ignored
tank    = Unit("tank", 150)

wraith  = Unit("wraith", 80)
print("[wraith] name: {0}, hp: {1}".format(wraith.name, wraith.hp))

wraith2 = Unit("wraith2", 100)
wraith2.isEnable = True              # You can add member variable outside of the class!
print("[wraith2] name: {0}, hp: {1}, isEnable: {2}".format(wraith2.name, wraith2.hp, wraith2.isEnable))

print("\n--------------------------------------\n")

# Inheritance

class AttackUnit(Unit): # AttackUnit(child class), Unit(parent class)
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : attack enemies to {1}. [damage: {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : is damaged by {1}".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{0} is destroyed".format(self.name))

firebat = AttackUnit("firebat", 50, 16)
firebat.attack("western east")
firebat.damaged(25)
firebat.damaged(25)

print("\n--------------------------------------\n")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} flys to {1} [speed: {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("valkyrie", 100, 10, 20)
valkyrie.fly(valkyrie.name, "3")