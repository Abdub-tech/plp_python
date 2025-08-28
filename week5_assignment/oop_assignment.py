# Assignment 1: Design Your Own Class! 🏗️

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")


# Inherited class (Inheritance 👑)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_type):
        super().__init__(brand, model, storage)
        self.strap_type = strap_type

    def info(self):
        # Polymorphism (overriding parent method 🎭)
        print(f"Smartwatch - Brand: {self.brand}, Model: {self.model}, Strap: {self.strap_type}")


# Activity 2: Polymorphism Challenge 🎭
class Animal:
    def move(self):
        print("Animal is moving 🐾")

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    # Assignment 1 demo
    phone = Smartphone("Samsung", "Galaxy S23", 256)
    phone.info()
    phone.call("+254700123456")

    watch = Smartwatch("Apple", "Watch Series 9", 32, "Leather")
    watch.info()
    watch.call("+254711223344")

    print("\n--- Polymorphism Demo ---")
    animals = [Dog(), Bird(), Fish()]
    for animal in animals:
        animal.move()
