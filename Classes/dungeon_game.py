import random

class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
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

class CaveEntrance(Scene):
    def enter(self):
        print("You stand at the entrance to a cave.)
        print("Wondering what is inside, you enter.")
        print("You see two paths inside the cave.")
        action = input("Do you go right or left?")
        if "right" in action.lower():
            print("You choose to go down the right tunnel")
            return "right_tunnel"
        elif "left" in action.lower():
            print("You choose to go down the left tunnel")
            return "left_tunnel"
        else:
            print("Action is not allowed")
            return  cave_entrance

class LeftTunnel(Scene):
    def enter(self):
        pass

class RightTunnel(Scene):
    def enter(self):
        pass

class Treasure(Scene):
    def enter(self):
        print("You find a treasure chest full of gold!")
        print("You return home happy, and very very rich.")
        return "end_game"

class Map(object):
    scenes = {
            'cave_enterance' : CaveEntrance()
            'left_tunnel' : LeftTunnel()
            'right_tunnel' : RightTunnel()

    }
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
