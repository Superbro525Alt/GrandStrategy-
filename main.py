#conquest

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
    def __init__(self, type=None, training=None, owner=None):
        self.type = type
        self.training = training
        self.owner = owner
        self.army = army
        self.army.append(self)

    def attack(self, otherUnit):
        if otherUnit.type == 'melee':
            if otherUnit.training == 'soldier':
                otherUnit.owner.army.remove(otherUnit)
                otherUnit.owner = None
            elif otherUnit.training == 'knight':
                self.owner.army.remove(self)
                self.owner = None
            elif otherUnit.training == 'archer':
                self.owner.army.remove(self)
                self.owner = None
        elif otherUnit.type == 'ranged':
            if otherUnit.training == 'soldier':
                self.owner.army.remove(self)
                self.owner = None
            elif otherUnit.training == 'knight':
                self.owner.army.remove(self)
                self.owner = None
            elif otherUnit.training == 'archer':
                otherUnit.owner.army.remove(otherUnit)
                otherUnit.owner = None
        elif otherUnit.type == 'siege':
            if otherUnit.training == 'soldier':
                self.owner.army.remove(self)
                self.owner = None
            elif otherUnit.training == 'knight':
                self.owner.army.remove(self)
                self.owner = None
            elif otherUnit.training == 'archer':
                self.owner.army.remove(self)
                self.owner = None
    def __str__(self):
        return {'type': self.type, 'training': self.training, 'owner': self.owner, 'army': self.army}
class meleeSoldier(troop):
    def __init__(self, owner=None):
        super().__init__(type='melee', training='soldier', owner=owner)
    def attack(self, otherUnit):
        super().attack(otherUnit)

class rangedSoldier(troop):
    def __init__(self, owner=None):
        super().__init__(type='ranged', training='soldier', owner=owner)
    def attack(self, otherUnit):
        super().attack(otherUnit)

class mortar(troop):
    def __init__(self, owner=None):
        super().__init__(type='artillery', training='mortar', owner=owner)
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

class map():
    def __init__(self, cities=[]):
        self.cities = cities
    def __str__(self):
        return {'cities': self.cities}

