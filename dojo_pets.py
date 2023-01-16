import dojo_pets_class_pet
class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet={"name": "dog" , "Type": "doberman" , "tricks": "play dead" } ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        if pet["Type"] == "dog":
            self.pet = dojo_pets_class_pet.Dog(pet["name"],pet["Type"], pet["tricks"], pet["breed"])
        elif pet["Type"] == "cat":
            self.pet = dojo_pets_class_pet.Cat(pet["name"],pet["Type"], pet["tricks"], pet["breed"])
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self 
    def bathe(self):
        self.pet.noise()
        return self

#print(locals())
#import DojoPetsClassPet



    
# implement the following methods:
#walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
#bathe() - cleans the ninja's pet invoking the pet noise() method






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
dojo_pets_class_pet.Cat.display_cats()
dojo_pets_class_pet.Pet.display_pets()
dojo_pets_class_pet.Dog.display_dogs()
