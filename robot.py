from dinosaur import Dinosaur


class Robot:
    def __init__(self, name, health, active_weapon):
        self.name = name
        self.health = health
        self.active_weapon = active_weapon

    def attack(self, target):
        if isinstance(target, Dinosaur):
            target.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
