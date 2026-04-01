class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)

robot1 = Robot("R2-D2")
robot2 = Robot("C-3PO")

robot1.introduce()
robot2.introduce()