class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        return "My name is {}.".format(self.name)


class Person:
    robotOwned = None

    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


r1 = Robot("Tom", "red", 30)
p1 = Person("Alice", "Aggressive", False)
p1.robotOwned = r1
print(p1.robotOwned.introduce_self())
