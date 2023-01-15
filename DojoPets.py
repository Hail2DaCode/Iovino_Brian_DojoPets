class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet={"name": "dog" , "Type": "doberman" , "tricks": "play dead" } ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        if pet["Type"] == "dog":
            self.pet = Dog(pet["name"],pet["Type"], pet["tricks"], pet["breed"])
        elif pet["Type"] == "cat":
            self.pet = Cat(pet["name"],pet["Type"], pet["tricks"], pet["breed"])
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
    pets = []
    def __init__(self, name , Type , tricks, ):
        self.name = name
        self.type = Type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        Pet.pets.append({f"name: {name}, Type: {Type}, tricks: {tricks},"})
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def noise(self):
        print("This is the pet's noise")
    @classmethod
    def display_pets(cls):
        for pet in Pet.pets:
            print(pet)

class Cat(Pet):
    cats = []
    def __init__(self, name, Type, tricks, breed="cat" ):
        super().__init__(name, Type, tricks)
        self.breed = breed
        Cat.cats.append({f"name: {name}, Type: {Type}, tricks: {tricks}, breed: {breed}"})
    def sleep(self):
        super().sleep()
    def eat(self):
        super().eat()
    def play(self):
        super().play()
    def noise(self):
        print("Meow")
    @classmethod
    def display_cats(cls):
        for cat in Cat.cats:
            print(cat)

class Dog(Pet):
    dogs = []
    def __init__(self, name, Type, tricks, breed="dog" ):
        super().__init__(name, Type, tricks)
        self.breed = breed
        Dog.dogs.append({f"name: {name}, Type: {Type}, tricks: {tricks}, breed: {breed}"})
    def sleep(self):
        super().sleep()
    def eat(self):
        super().eat()
    def play(self):
        super().play()
    def noise(self):
        print("Wuff")
    @classmethod
    def display_dogs(cls):
        for dog in Dog.dogs:
            print(dog)
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
ninja_1 = Ninja("Brian", "Doe", "sugar", "meat", {"name": "Buttons", "Type": "cat", "tricks": "purr", "breed": "Burmese"})
ninja_2 = Ninja("Michael", "Doe", "fish", "tuna", {"name": "Tiger", "Type": "cat", "tricks": "nibble", "breed": "British shorthair"})
ninjas_3 = Ninja("Vincent", "Doe", "chopped liver", "meat", {"name": "Rocky", "Type": "dog", "tricks": "roll over", "breed": "husky"})
print(ninja_1.pet.health)
ninja_1.walk().feed().bathe()
print(ninja_1.pet.health)
print(ninja_1.pet.energy)
print(ninja_1.pet.breed)
Cat.display_cats()
Pet.display_pets()
Dog.display_dogs()