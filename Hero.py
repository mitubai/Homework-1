class SuperHero:
    # Свойство класса
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f'Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Кларк Кент', 'Супермен', 'Полёт, сверхсила', 100, 'Вверх, и только вверх!')
print(hero)
print('Длина коронной фразы:', len(hero))
hero.double_health()
print('Здоровье после удвоения:', hero.health_points)
