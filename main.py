#conquest
import eel
import sys
import pickle
class player():
    def __init__(self, control=[], name=None, bot=False, units=[], map=None, country=None):
        self.control = []
        self.country = country
        self.name = name
        self.bot = bot
        self.score = 0
        self.units = units
        self.game = game
        self._map = map
        for c in control:
            self.control.append(c)


    def __str__(self):
        return {'control': self.control, 'name': self.name, 'bot': self.bot, 'score': self.score}

    def get(self):
        return self.__str__()
    def init(self):
        for i in range(len(self._map.cities)):
            #print(self._map.cities[i].owner)
            try:
                if self._map.cities[i].owner.name == self.name:
                    self.control.append(self._map.cities[i])
                    self.score += self._map.cities[i].score
            except AttributeError:
                pass
        for i in range(len(self.control)):
            if self.control[i].owner.name != self.name:
                self.score -= self.control[i].score
                self.control.remove(self.control[i])


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

    def create(self, city, type=None):
        if type == None:
            self.units.append(troop(owner=self, city=city))
        else:
            if type == 'melee':
                self.units.append(meleeSoldier(owner=self, city=city))
            elif type == 'ranged':
                self.units.append(rangedSoldier(owner=self, city=city))
            elif type == 'mortar':
                self.units.append(mortar(owner=self, city=city))


    def botTick(self):
        if self.bot:
            for i in range(len(self.control)):
                if self.control[i].owner == self:
                    print('bot ai here')
class troop():
    def __init__(self, type=None, training=None, owner=None, city=None):
        self.type = type
        self.training = training
        self.owner = owner
        self.hp = 100
        self.city = city
        self.city.army.append(self)
    
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
        super().__init__(type='melee', training='meleeSoldier', owner=owner)
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
    def __init__(self, players=[], map=None, name=None):
        self.players = players
        self._map = map
        self.name = name
    def __str__(self):
        return {'players': self.players, 'map': self.map}
    def init(self):
        for i in range(len(self.players)):
            self.players[i].init()

    def tick(self):
        for player_ in self.players:
            player_.botTick()

class manager():
    def __init__(self, settings={}, path='/games/games.pickle', settingsPath='/games/settings.pickle'):
        self.settings = settings
        self.path = sys.path[0] + path
        self.settingsPath = sys.path[0] + settingsPath
    def saveGame(self, game):
        temp = pickle.load(open(self.path, 'rb'))
        k = list(temp.keys())
        v = list(temp.values())

        k.append(game.name)
        v.append(game)

        temp = dict(zip(k, v))
        pickle.dump(temp, open(self.path, 'wb'))

    def loadGame(self, name):
        return pickle.load(open(self.path, 'rb'))[name]
    def deleteGame(self, name):
        temp = pickle.load(open(self.path, 'rb'))
        del temp[name]
        pickle.dump(temp, open(self.path, 'wb'))
    def loadSettings(self):
        return pickle.load(open(self.settingsPath, 'rb'))
    def saveSettings(self, settings):
        pickle.dump(settings, open(self.settingsPath, 'wb'))

    def list(self):
        return pickle.load(open(self.path, 'rb'))

    def __str__(self):
        return {'settings': self.settings, 'path': self.path}

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(list(self.list().values()))

    def createGame(self, name, players, map):
        self.saveGame(game(name=name, players=players, map=map))
        return self.loadGame(name)

    def init(self):
        try:
            pickle.load(open(self.path, 'rb'))
        except:
            pickle.dump({}, open(self.path, 'wb'))


@eel.expose
def openHtml(path):
    eel.start(path, port=60)
    return 0


def init(htmlpath):
    global lastport
    lastport = 0
    eel.init(htmlpath)

m = manager()

@eel.expose
def makeGame(name, country=None, map=map([city(name='c1', x=0, y=0)])):
    print('making')
    return m.createGame(name, [player(name='p1', country=country)], map)

@eel.expose
def loadGame(name):
    return m.loadGame(name)

@eel.expose
def listGamesValues():
    return list(m.list().values())

@eel.expose
def listGamesKeys():
    print(list(m.list().keys()))
    return list(m.list().keys())

m.init()
print(m.list())
init('html')
openHtml('index.html')




