import random


class Robot:
    def __init__(self, name, *weapons):
        self.name = name
        self.health = random.randint(100, 500)
        self.weapons = weapons
        self.attack_power = None
        self.weapon = None

    def choose_weapon(self):
        # Choose a weapon from the list of weapons
        self.weapon = random.choice(self.weapons)
        print(f"{self.name} has chosen the {self.weapon.name} weapon.")
        self.attack_power = self.weapon.attack_power
        return self.weapon

    def attack(self, target):
        if isinstance(target, Dinosaur):
            target.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage


class Dinosaur:
    def __init__(self, name, *weapons):
        self.name = name
        self.health = random.randint(100, 500)
        self.weapons = weapons
        self.attack_power = None
        self.weapon = None

    def choose_weapon(self):
        # Choose a weapon from the list of weapons
        self.weapon = random.choice(self.weapons)
        print(f"{self.name} has chosen the {self.weapon.name} weapon.")
        self.attack_power = self.weapon.attack_power
        return self.weapon

    def attack(self, target):
        if isinstance(target, Robot):
            target.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage


class Fleet:
    def __init__(self, *robots):
        self.robots = robots


class Herd:
    def __init__(self, *dinosaurs):
        self.dinosaurs = dinosaurs
