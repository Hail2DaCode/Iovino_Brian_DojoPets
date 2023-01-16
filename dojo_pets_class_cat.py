import dojo_pets_class_pet
class Cat(dojo_pets_class_pet.Pet):
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