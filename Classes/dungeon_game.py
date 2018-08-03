import random

class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print("\n--------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    quips = ["You died. Better luck next time.",
                   "Ba Boom! You dead man!",
                   "Dead as a door-knob. Maybe you should take up knitting instead."]

    def enter(self):
        print(random.choice(self.quips))
        exit()

class OpeningScene(Scene):
    def enter(self):
        print("You stand at the entrance to a cave.")
        print("Wondering what is inside, you enter.")
        return "cave_entrance"

class CaveEntrance(Scene):
    def enter(self):
        print("You see two paths inside the cave.")
        action = input("Do you go right or left? ")
        if "right" in action.lower():
            print("You choose to go down the right tunnel")
            input("Enter to continue")
            return "goblin"
        elif "left" in action.lower():
            print("You choose to go down the left tunnel")
            input("Enter to continue")
            return "dragon_lair"
        elif "i win" in action.lower():
            return 'treasure_trove'
        else:
            print("Action is not allowed")
            input("Enter to continue")
            return  'cave_entrance'

class DragonLair(Scene):
    def enter(self):
        print("You come to a large pit.")
        print("You look down into the pit and feel a strange source of heat.")
        print("A dragon suddenly appears out of the pit")

        action = input("Do you run or fight? ")
        if "run" in action:
            print("You run back the way you came.")
            input("Enter to continue")
            return 'cave_entrance'
        elif "fight" in action:
            print("You ball up your fist and punch the dragon square in the nose")
            print("The dragon opens his mouth incinerates your flesh.")
            input("Enter to continue")
            return "death"
        else:
            print("Not a valid action")
            input("Enter to continue")
            return "dragon_lair"


class TreasureTrove(Scene):
    def enter(self):
        print("You find a treasure chest full of gold!")
        print("You return home happy, and very very rich.")
        exit()

class Goblin(Scene):
    def enter(self):
        print("You meet a goblin")
        action = input("Fight or flee?")
        if "fight" in action.lower():
            print("You rush the goblin, who disappears.")
            return 'treasure_trove'
        elif "flee" in action.lower():
            print("You run away")
            return 'cave_entrance'
        else:
            print("Invalid input")
            return 'goblin'

class Map(object):
    scenes = {
            'opening_scene' : OpeningScene(),
            'cave_entrance' : CaveEntrance(),
            'dragon_lair' : DragonLair(),
            'treasure_trove' : TreasureTrove(),
            'death' : Death(),
            'goblin' : Goblin()
            }


    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)
    def opening_scene(self):
        return self.next_scene(self.start_scene)

if __name__ == "__main__":
    a_map = Map('opening_scene')
    a_game = Engine(a_map)
    a_game.play()
