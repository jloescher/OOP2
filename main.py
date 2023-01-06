from participants import Robot, Dinosaur, Fleet, Herd
from battlefield import Battlefield
from weapon import Weapon


def main():
    # Create some weapons
    laser = Weapon("Laser")
    plasma_cannon = Weapon("Plasma Cannon")
    mini_gun = Weapon("Mini Gun")
    rail_gun = Weapon("Rail Gun")
    rocket_launcher = Weapon("Rocket launcher")
    ion_cannon = Weapon("Ion cannon")
    fist = Weapon("Fist")
    tail = Weapon("Tail")
    claws = Weapon("Claws")
    bite = Weapon("Bite")

    # Create some robots
    robot1 = Robot("Bender", laser, rail_gun, mini_gun)
    robot2 = Robot("Wall-E", plasma_cannon, laser, rail_gun)
    robot3 = Robot("R2-D2", rail_gun, mini_gun, plasma_cannon)
    robot4 = Robot("K-2SO", laser, mini_gun)
    robot5 = Robot("Atlas", rocket_launcher, ion_cannon, plasma_cannon)
    robot6 = Robot("Marvin", laser, mini_gun, plasma_cannon, rocket_launcher)

    # Create a fleet
    fleet = Fleet(robot3, robot4, robot6)

    # Create some dinosaurs
    dinosaur1 = Dinosaur("Rexy", fist, bite)
    dinosaur2 = Dinosaur("Littlefoot", fist, claws)
    dinosaur3 = Dinosaur("Petrie", tail, claws)
    dinosaur4 = Dinosaur("Arlo", fist, tail)
    dinosaur5 = Dinosaur("Blue", tail, fist)
    dinosaur6 = Dinosaur("Indoraptor", tail, bite)

    # Create a herd
    herd = Herd(dinosaur3, dinosaur4, dinosaur5)

    # # Create a battlefield
    # battlefield = Battlefield()

    # # Add the robots and dinosaurs to the battlefield
    # battlefield.add_participants(
    #     robot1, robot2, robot5, dinosaur1, dinosaur2, dinosaur6
    # )

    # # Start the battle
    # battlefield.start_battle()

    battlefield_2 = Battlefield()

    battlefield_2.add_participants(fleet, herd)

    battlefield_2.start_battle()


if __name__ == "__main__":
    main()
