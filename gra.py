import random
################################################################################
#Definiowanie wartości początkowych
################################################################################


#słownik definiujący premię ataku za typ postaci
battle_dict = {
    'AA':0, 'AB':1, 'AC':0, 'AD':-1,
    'BA':-1, 'BB':0, 'BC':1, 'BD':0,
    'CA':0, 'CB':-1, 'CC':0, 'CD':1,
    'DA':1, 'DB':0, 'DC':-1, 'DD':0
    }


################################################################################
#KLASY BOHATERÓW
################################################################################


class HERO(object):

#słownik definiujący premię ataku i kary obrony za posiadaną broń
    weapon_type = {'karabinlaserowy':{'attack':2, 'defence':-1},
        'dzidalaserowa':{'attack':2,'defence':0},
        'chujowedziałko':{'attack':1, 'defence':0},
        'dzidanormalna':{'attack':1, 'defence':0},
        'biczlaserowy':{'attack':1, 'defence':0}
        }

#słownik definiujący karę ataku i premię obrony za posiadany pancerz
    armor_type = {'tarczalaserowa':{'attack':-1, 'defence':2},
        'gwiezdnyparasol':{'attack':0, 'defence':1},
        'kombinezonbojowy':{'attack':0, 'defence':1},
        'hełm':{'attack':0, 'defence':1},
        'zbrojasultana':{'attack':0, 'defence':2}
        }

    def __init__(self, lvl, health, weapon, armor):#atrybuty początkowe
        self.lvl = lvl
        self.health = health
        self.weapon = weapon
        self.armor = armor

#siła broni: premia ataku za posiadaną broń i kara za posiadany pancerz + premia za lvl
    def attack_power(self):
        weapon_power = self.weapon_type[self.weapon]['attack'] + self.armor_type[self.armor]['attack'] + self.lvl
        self.weapon_power = weapon_power

#siła obrony: premia obrony za posiadany pancerz i kara za posiadaną broń +premia za lvl
    def defence_power(self):
        armor_power = self.armor_type[self.armor]['defence'] + self.weapon_type[self.weapon]['defence'] + self.lvl
        self.armor_power = armor_power
class GENERALLUFA(HERO):
    TYPE = 'A'

class KAPITANBOMBA(HERO):
    TYPE = 'B'

class ADMIRALJACHAS(HERO):
    TYPE = 'C'

class CHORAZYTORPEDA(HERO):
    TYPE = 'D'


################################################################################
#KLASY POTWORÓW
################################################################################


class MONSTER(object):

    def __init__(self):
        self.lvl = random.randint(0, 3)
        self.wpower = random.randint(-1, 2)
        self.apower = random.randint(-1, 2)
        self.attack = self.lvl + self.wpower
        self.defence = self.lvl + self.apower

class KURWINOX(MONSTER):
    TYPE = 'A'

class SKURWOL(MONSTER):
    TYPE = 'B'

class KUTANOID(MONSTER):
    TYPE = 'C'

class CQRWOZAUR(MONSTER):
    TYPE = 'D'


################################################################################
#WALKA
################################################################################

#używane, kiedy bohater decyduje się zaatakować potwora
class attack(object):
    def __init__(self, PLAYER, ENEMY):
        self.player_type = PLAYER.TYPE #typ bohatera (A, B, C, D)
        self.enemy_type = ENEMY.TYPE #typ przeciwnika
        #obliczanie bonusu do ataku wynikającego z typu postaci i przeciwnika
        self.bonus = battle_dict['{}{}'.format(self.player_type, self.enemy_type)]
        PLAYER.attack_power #init funkcji attack_power
        #siła ataku bohatera, czyli premia za broń i lvl + bonus za typ + randint
        self.hero_attack_power = PLAYER.weapon_power + self.bonus + random.randint(0, 3)
        #siła obrony potwora + randint
        self.monster_defence_power = ENEMY.defence + random.randint(0, 3)
        if self.hero_attack_power >= self.monster_defence_power:
            print("win")
        elif self.attack_power < self.defence_power:
            print("loose")

#używane, kiedy potwór zaatakuje bohatera
class defence(attack):
    def __init__(self, PLAYER, ENEMY):
        #bonus za typ
        self.bonus = battle_dict['{}{}'.format(self.enemy_type, self.player_type)]
        #siła ataku potwora: siła broni + bonus + randint
        self.monster_attack_power = ENEMY.atack + self.bonus + random.randint(0, 3)
        PLAYER.defence_power #init funkcji defence power
        #siła obrony bohatera czyli premia za pancerz i lvl + randint
        self.hero_defence_power = PLAYER.armor_power + random.rabdint(0, 3)
        if self.monster_attack_power >= self.hero_defence_power:
            print("loose")
        elif self.monster_attack_power < self.hero_defence_power:
            print("win")

# (_)_)==================D TEST
#def test():
#    a = KAPITANBOMBA(20, 10, 'karabinlaserowy', 'hełm')
#    a.attack_power()
#    a.defence_power()
#    return a

#a = test()
