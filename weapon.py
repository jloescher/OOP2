import random


class Weapon:
    def __init__(self, name):
        self.name = name
        self.attack_power = random.randint(1, 150)
