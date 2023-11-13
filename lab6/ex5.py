class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display_info(self):
        return f"Name: {self.name}, Habitat: {self.habitat}"


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def display_info(self):
        return f"{super().display_info()}, Fur Color: {self.fur_color}"

    def give_birth(self):
        return f"{self.name} is a mammal and gives birth to live young."


class Bird(Animal):
    def __init__(self, name, habitat, feather_color):
        super().__init__(name, habitat)
        self.feather_color = feather_color

    def display_info(self):
        return f"{super().display_info()}, Feather Color: {self.feather_color}"

    def lay_eggs(self):
        return f"{self.name} is a bird and lays eggs."


class Fish(Animal):
    def __init__(self, name, habitat, scale_type):
        super().__init__(name, habitat)
        self.scale_type = scale_type

    def display_info(self):
        return f"{super().display_info()}, Scale Type: {self.scale_type}"

    def lay_eggs(self):
        return f"{self.name} is a fish and lays eggs."


mammal = Mammal(name="Lion", habitat="Grasslands", fur_color="Golden")
print(mammal.display_info())
print(mammal.give_birth())

bird = Bird(name="Eagle", habitat="Mountains", feather_color="Brown")
print(bird.display_info())
print(bird.lay_eggs())

fish = Fish(name="Salmon", habitat="Freshwater", scale_type="Scales")
print(fish.display_info())
print(fish.lay_eggs())
