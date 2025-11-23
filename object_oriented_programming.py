class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def greet(self):
        return f'Feck off {self.name}'

def access_person():
    person: Person = Person('Jack', 24)
    print(person.greet())

class Animal:
    def sound(self):
        return 'Noise'

# Inheritance
class Dog(Animal):
    # Override
    def sound(self):
        return 'Bark'

class Box:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Box({self.value})'

    def __len__(self):
        return len(self.value)

class MathOps:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return "MathOps class"

def class_with_static_methods():
    r1 = MathOps.add(1, 2)
    r2 = MathOps.info()
    print(f'Static add class.method(): {r1}')
    print(f'Static add class.info(): {r2}')
