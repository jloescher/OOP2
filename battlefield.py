import random


class Battlefield:
    def __init__(self, participants):
        self.participants = []

    def add_participants(self, *participants):
        self.participants.extend(participants)

    def start_battle(self):
        while any(p.health > 0 for p in self.participants):
            for attacker in self.participants:
                if attacker.health <= 0:
                    continue
                targets = [
                    p for p in self.participants if p.health > 0 and p != attacker
                ]
                if not targets:
                    break
                target = random.choice(targets)
                attacker.attack(target)
