import dojo_pets_class_pet
class Dog(dojo_pets_class_pet.Pet):
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