class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def true_in_true_phrase(self):
        print("True in the True_phrase")

    def __str__(self):
        return f'Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


class Earth_Terrain_Hero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)
        self.terrain = 'earth'

    def double_health(self):
        self.health_points **= 2
        self.fly = True


class Air_Terrain_Hero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)
        self.terrain = 'air'

    def double_health(self):
        self.health_points **= 2
        self.fly = True


class Villain(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)
        self.people = 'monster'
    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2


superman = SuperHero('Кларк Кент', 'Супермен', 'Полёт, сверхсила', 100, 'Вверх, и только вверх!', 10)
earth_hero = Earth_Terrain_Hero('Иван', 'Земляной', 'Управление землёй', 80, 'Земля - моя сила!', 15)
air_hero = Air_Terrain_Hero('Алекс', 'Воздушный', 'Управление воздухом', 90, 'Ветер мой союзник!', 20)

villain = Villain('Джокер', 'Клоун', 'Манипуляции, химия', 150, 'Ха-ха-ха!', 30)

superman.double_health()
superman.true_in_true_phrase()
print(superman)

earth_hero.double_health()
earth_hero.true_in_true_phrase()
print(earth_hero)

air_hero.double_health()
air_hero.true_in_true_phrase()
print(air_hero)

villain.crit()
villain.true_in_true_phrase()
print(villain)
print("Villain's damage after crit:", villain.damage)
