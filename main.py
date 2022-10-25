#conquest

class player():
    def __init__(self, control=[], name=None, bot=False, units=[]):
        self.control = control
        self.name = name
        self.bot = bot
        self.score = 0
        self.units = units


    def __str__(self):
        return {'control': self.control, 'name': self.name, 'bot': self.bot, 'score': self.score}

    def init(self):
        for i in range(len(g._map.cities)):
            if g._map.cities[i].owner == self:
                self.control.append(g._map.cities[i])

    def capture(self, city):
        self.control.append(city)
        city.owner = self
        city.army = []
    def goForCapture(self, city):
        if city.owner == None:   
            self.capture(city)
            self.score += city.score
        else:
            self.attack(city)
            self.score += city.score

    def attack(self, city, units=None):
        if units != None:
            count = 0
            for i in range(len(self.units)):
                if self.units[i].attack(city.army[count]):
                    count += 1
                    
    def move(self, city, units):
        for i in range(len(units)):
            city.army.append(units[i])
            self.units[i].city.army.remove(units[i])

    def train(self, city, type=None):
        if type == None:
            self.units.append(troop(owner=self, city=city))
        else:
            self.units.append(type(owner=self, city=city))
class troop():
    def __init__(self, type=None, training=None, owner=None, city=None):
        self.type = type
        self.training = training
        self.owner = owner
        self.hp = 100
        self.city = city
    
    def tick(self):
        if self.hp < 1:
            self.owner.army.remove(self)
            self.owner = None
            return False
        else:
            return True

    def attack(self, otherUnit):
        if otherUnit.type == 'melee':
            if otherUnit.training == 'soldier':
                otherUnit.hp -= 10
                return self.tick()
            elif otherUnit.training == 'knight':
                self.hp -= 10
                return self.tick()
            elif otherUnit.training == 'archer':
                self.hp -= 10
                return self.tick()
        elif otherUnit.type == 'ranged':
            if otherUnit.training == 'soldier':
                self.hp -= 10
                return self.tick()
            elif otherUnit.training == 'knight':
                self.hp -= 10
                return self.tick()
            elif otherUnit.training == 'archer':
                otherUnit.hp -= 10
                return self.tick()
        elif otherUnit.type == 'siege':
            if otherUnit.training == 'soldier':
                self.hp -= 10
                return self.tick()
            elif otherUnit.training == 'knight':
                self.hp -= 10
                return self.tick()
            elif otherUnit.training == 'archer':
                self.hp -= 10
                return self.tick()
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
    def __init__(self, name=None, owner=None, army=[], x=None, y=None, artPath=None, score=1):
        self.name = name
        self.owner = owner
        self.army = army
        self.x = x
        self.y = y
        self.artPath = artPath
        self.score = score
    def render(self):
        if self.artPath == None:
            return None, self.x, self.y
        else:
            return self.artPath, self.x, self.y

    def __str__(self):
        return {'name': self.name, 'owner': self.owner, 'army': self.army, 'x': self.x, 'y': self.y}

class map():
    def __init__(self, cities=[]):
        self.cities = cities
    def __str__(self):
        return {'cities': self.cities}

class game():
    def __init__(self, players=[], map=None):
        self.players = players
        self._map = map
    def __str__(self):
        return {'players': self.players, 'map': self.map}
    def init(self):
        for i in range(len(self.players)):
            g.players[i].init()

def test():
    p = player(name='player1', units=[meleeSoldier(), rangedSoldier(), mortar()])
    p2 = player(name='player2', units=[meleeSoldier(), rangedSoldier(), mortar()])

    c = city(name='city1', owner=p, army=[meleeSoldier(), rangedSoldier(), mortar()], x=0, y=0)
    c2 = city(name='city2', owner=None, army=[meleeSoldier(), rangedSoldier(), mortar()], x=0, y=0)

    m = map(cities=[c, c2])

    g = game(players=[p, p2], map=m)

    g.init()

    p.goForCapture(c2)

    print(p.control)

if __name__ == '__main__':
    test()
