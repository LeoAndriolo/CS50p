# Set 8 Class - Types of Python

import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]   # Class variable

    @classmethod    # Class method
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

    # def __init__(self) -> None:
    #     self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # def sort(self, name):
    #     print(name, "is in", random.choice(self.houses))


Hat.sort("Harry")