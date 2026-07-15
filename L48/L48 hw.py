class Cat:
    def __init__(self, nm, h): #cat constructor
        self.name = nm
        self.age = h

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("meow")

class Dog:
    def __init__(self, nm, h): #dog constructor
        self.name = nm
        self.age = h
    
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Woof Woff")

cat1 = Cat("Kitten", 2.5)
dog1 = Dog("Frenzy", 3)

for animal in (dog1, cat1): #representing cat1 and dog1 as animal
    animal.make_sound()
    animal.info()
    print()