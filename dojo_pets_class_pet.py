#import DojoPets
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

print(locals())
print(__name__)
if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
  
'''ninja_1 = Ninja("Brian", "Doe", "sugar", "meat", {"name": "Buttons", "Type": "cat", "tricks": "purr", "breed": "Burmese"})
ninja_2 = Ninja("Michael", "Doe", "fish", "tuna", {"name": "Tiger", "Type": "cat", "tricks": "nibble", "breed": "British shorthair"})
ninjas_3 = Ninja("Vincent", "Doe", "chopped liver", "meat", {"name": "Rocky", "Type": "dog", "tricks": "roll over", "breed": "husky"})
print(ninja_1.pet.health)
ninja_1.walk().feed().bathe()
print(ninja_1.pet.health)
print(ninja_1.pet.energy)
print(ninja_1.pet.breed)
Cat.display_cats()
Pet.display_pets()
Dog.display_dogs()'''
