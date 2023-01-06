import random
from participants import Dinosaur, Herd, Fleet, Robot


class Battlefield:
    def __init__(self):
        self.participants = []
        self.round_count = 0

    def add_participants(self, *participants):
        self.participants.extend(participants)

    def select_target(self, attacker, targets):
        targets_to_attack = []
        # Select a target from the list of potential targets
        for target in targets:
            if isinstance(target, Fleet):
                for robot in target.robots:
                    if robot != attacker:
                        targets_to_attack.append(robot)
            elif isinstance(target, Herd):
                for dino in target.dinosaurs:
                    if dino != attacker:
                        targets_to_attack.append(dino)
            elif isinstance(target, (Dinosaur, Robot)):
                if target != attacker:
                    targets_to_attack.append(target)

        target = random.choice(targets_to_attack)
        return target

    def alive_participants(self):
        alive_list = []
        for p in self.participants:
            if isinstance(p, (Robot, Dinosaur)) and p.health > 0:
                alive_list.append(p)
            elif isinstance(p, Fleet):
                for bot in p.robots:
                    if bot.health > 0:
                        alive_list.append(bot)
            elif isinstance(p, Herd):
                for dino in p.dinosaurs:
                    if dino.health > 0:
                        alive_list.append(dino)
        return alive_list

    def conclude_battle(self):
        # Determine the number of alive participants
        alive_participants = self.alive_participants()
        num_alive = len(alive_participants)

        # If there is only one participant left, they are the winner
        if num_alive == 1:
            winner = alive_participants[0]
            print(f"{winner.name} has won the battle!")
            return winner

        # If there are no participants left, the battle is a tie
        elif num_alive == 0:
            print("All of the dinosaurs and robots are dead.")
            return num_alive

        # If there are multiple participants left and they are all robots, the robots win
        elif all(isinstance(p, Robot) for p in alive_participants):
            print("All robots have won the battle!")
            return alive_participants

        # If there are multiple participants left and they are all robots, the robots win
        elif all(isinstance(p, Dinosaur) for p in alive_participants):
            print("All dinosaurs have won the battle!")
            return alive_participants

        # If there are multiple participants left and they are all dinosaurs or robots, they both win
        elif all(
            isinstance(p, type(alive_participants[0])) for p in alive_participants
        ):
            print("Both dinosaurs and robots have won the battle!")
            return alive_participants

        # If there are multiple participants left, the battle is still ongoing
        else:
            print("The battle is still ongoing.")
            return None

    def start_battle(self):
        while True:
            for attacker in self.participants:
                if isinstance(attacker, Fleet):
                    # Choose a weapon for each robot in the fleet
                    for robot in attacker.robots:
                        robot.choose_weapon()
                    # Attack with all robots in the fleet
                    for robot in attacker.robots:
                        target = self.select_target(robot, self.participants)
                        robot.attack(target)

                elif isinstance(attacker, Herd):
                    # Choose a weapon for each dinosaur in the herd
                    for dino in attacker.dinosaurs:
                        dino.choose_weapon()
                    # Attack with all dinosaurs in the herd
                    for dino in attacker.dinosaurs:
                        target = self.select_target(dino, self.participants)
                        dino.attack(target)
                elif isinstance(attacker, (Robot, Dinosaur)) and attacker.health <= 0:
                    continue
                else:
                    # Choose a weapon for the attacker
                    attacker.choose_weapon()
                    targets = [
                        p for p in self.participants if p.health > 0 and p != attacker
                    ]
                    if not targets:
                        break
                    target = random.choice(targets)
                    attacker.attack(target)

            # Check if the battle has ended
            winner = self.conclude_battle()
            if winner or winner == 0:
                break
