class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet={"name": "dog" , "type1": "doberman" , "tricks": "play dead" } ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(pet["name"],pet["type1"], pet["tricks"])
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self 
    def bathe(self):
        self.pet.noise()
        return self

        	
    
# implement the following methods:
#walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Pet:
    def __init__(self, name , type1 , tricks ):
        self.name = name
        self.type = type1
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def noise(self):
        print("This is the pet's noise")

class Cat:
    
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
ninja_1 = Ninja("Brian", "Iovino", "sugar", "meat", {"name": "Buttons", "type1": "cat", "tricks": "purr"})
print(ninja_1.pet.health)
ninja_1.walk().feed().bathe()
print(ninja_1.pet.health)
print(ninja_1.pet.energy)
