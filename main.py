#conquest
# -*- coding: python -*-
# -*- grand strategy -*-

class player():
    def __init__(self, control=[], name=None, bot=False):
        self.control = control
        self.name = name
        self.bot = bot
        self.score = 0

    def __str__(self):
        return {'control': self.control, 'name': self.name, 'bot': self.bot, 'score': self.score}

    def capture(self, city):
        self.control.append(city)
        city.owner = self
        city.army = []
    def goForCapture(self, city):
        if city.owner == None:
            self.capture(city)
        else:
            self.attack(city)
    def attack(self, city):
        raise NotImplementedError()

class troop():
    def __init__(self, type=None, training=None, owner=None, army=None):
        self.type = type
        self.training = training
        self.owner = owner
        self.army = army
        self.army.append(self)
    def attack(self, otherUnit):
        raise NotImplementedError()

class meleeSoldier(troop):
    def __init__(self, owner=None, army=None):
        super().__init__(type='melee', training='soldier', owner=owner, army=army)
    def attack(self, otherUnit):
        super().attack(otherUnit)

class rangedSoldier(troop):
    def __init__(self, owner=None, army=None):
        super().__init__(type='ranged', training='soldier', owner=owner, army=army)
    def attack(self, otherUnit):
        super().attack(otherUnit)

class artillery(troop):
    def __init__(self, owner=None, army=None):
        super().__init__(type='artillery', training='soldier', owner=owner, army=army)
    def attack(self, otherUnit):
        super().attack(otherUnit)
        

class city():
    def __init__(self, name=None, owner=None, army=[], x=None, y=None):
        self.name = name
        self.owner = owner
        self.army = army
        self.x = x
        self.y = y
    def __str__(self):
        return {'name': self.name, 'owner': self.owner, 'army': self.army, 'x': self.x, 'y': self.y}

print("change")





