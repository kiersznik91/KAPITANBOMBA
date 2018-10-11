import random
################Definiowanie wartości początkowych
hero_health = 10
lvl = 0
weapon = False
armor = False

weapon_type = {'karabinlaserowy':{'attack':2, 'defence':-1},
    'dzidalaserowa':{'attack':2,'defence':0},
    'chujowedziałko':{'attack':1, 'defence':0},
    'dzidanormalna':{'attack':1, 'defence':0},
    'biczlaserowy':{'attack':1, 'defence':0}
    }

armor_type = {'tarczalaserowa':{'attack':-1, 'defence':2},
    'gwiezdnyparasol':{'attack':0, 'defence':1},
    'kombinezonbojowy':{'attack':0, 'defence':1},
    'hełm':{'attack':0, 'defence':1},
    'zbrojasultana':{'attack':0, 'defence':2}
    }

battle_dict = {
    'AA':0, 'AB':1, 'AC':0, 'AD':-1,
    'BA':-1, 'BB':0, 'BC':1, 'BD':0,
    'CA':0, 'CB':-1, 'CC':0, 'CD':1,
    'DA':1, 'DB':0, 'DC':-1, 'DD':0
    }


################################KLASY BOHATERÓW

class HERO(object):
    def __init__(self, lvl, wpower, apower):
        self.lvl = lvl
        self.wpower =  wpower
        self.apower = apower
    def attack_power(self):
        self.attack = self.lvl + self.wpower
    def defense_power(self):
        self.defense = self.lvl + self.apower

class GENERALLUFA(HERO):
    TYPE = 'A'

class KAPITANBOMBA(HERO):
    TYPE = 'B'

class ADMIRALJACHAS(HERO):
    TYPE = 'C'

class CHORAZYTORPEDA(HERO):
    TYPE = 'D'


###############################KLASY POTWORÓW

class MONSTER(object):
    def __init__(self):
        self.lvl = random.randint(0, 3)
        self.wpower = random.randint(-1, 2)
        self.apower = random.randint(-1, 2)
    def attack_power(self):
        self.attack = self.lvl + self.wpower
    def defence_power(self):
        self.defence = self.lvl + self.apower

class KURWINOX(MONSTER):
    TYPE = 'A'

class SKURWOL(MONSTER):
    TYPE = 'B'

class KUTANOID(MONSTER):
    TYPE = 'C'

class CQRWOZAUR(MONSTER):
    TYPE = 'D'

###########################WALKA

class attack(object):
    def __init__(self, PLAYER, ENEMY):
        self.player_type = PLAYER.TYPE
        self.enemy_type = ENEMY.TYPE
        self.bonus = int(battle_dict[self.player_type + self.enemy_type])#nie działa xD
        self.attack_power = PLAYER.attack + self.bonus + random.randint(0, 3)
        self.defence_power = ENEMY.defence + random.randint(0, 3)
        if self.attack_power >= self.defence_power:
            win()
        elif self.attack_power < self.defence_power:
            loose()
    def win():
        print(1)

    def loose():
        print(2)

#tutaj widzę
