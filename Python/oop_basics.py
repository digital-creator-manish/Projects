class Animal:
    # Class variable
    kingdom = "Animalia"

    def __init__(self, name, sound):
        # Instance variables
        self.name = name
        self.sound = sound

    # Instance method
    def speak(self):
        print(f"{self.name} says {self.sound}")

    # Class method
    @classmethod
    def get_kingdom(cls):
        return cls.kingdom

    # Static method
    @staticmethod
    def is_animal(obj):
        return isinstance(obj, Animal)

# Inheritance example
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

# Usage
if __name__ == "__main__":
    cat = Animal("Cat", "Meow")
    dog = Dog("Buddy")

    cat.speak()           # Output: Cat says Meow
    dog.speak()           # Output: Buddy says Woof

    print(Animal.get_kingdom())  # Output: Animalia
    print(Animal.is_animal(cat)) # Output: True