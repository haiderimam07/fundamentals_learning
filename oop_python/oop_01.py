# in this i will be adding mainly syntax of the oop concept how to write classes how to creat objects and ll that and how take the pillars of oop in action with proper syntax these kind of thing 

"""
OOP IN PYTHON - SYNTAX + EXPLANATION
====================================
Sections:
    1. Classes and Objects
    2. Instance vs Class attributes
    3. Types of methods (instance, class, static)
    4. Magic (dunder) methods
    5. Pillar 1 - Encapsulation
    6. Pillar 2 - Inheritance
    7. Pillar 3 - Polymorphism
    8. Pillar 4 - Abstraction
    9. Bonus - Composition and dataclasses

Run the file to see the output of every section.
"""

# ============================================================
# 1. CLASSES AND OBJECTS
# ============================================================
# A CLASS is a blueprint. An OBJECT (instance) is a real thing built from it.
#
# Syntax:
#   class ClassName:
#       def __init__(self, params):   # constructor - runs when object is created
#           self.attribute = value    # instance attribute
#
#       def method(self):             # instance method - 'self' = the object itself
#           ...

print("=== 1. Classes and Objects ===")


class Dog:
    def __init__(self, name, age):
        self.name = name      # instance attributes (unique to each object)
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1         # methods can modify the object's own data


# Creating objects (instantiation)
dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

print(dog1.name)              # accessing an attribute -> Rex
print(dog2.bark())            # calling a method       -> Bella says Woof!
dog1.birthday()
print(dog1.age)               # 4

# Handy built-in functions
print(isinstance(dog1, Dog))  # True  - is dog1 an instance of Dog?
print(type(dog1))             # <class '__main__.Dog'>
print(hasattr(dog1, "name"))  # True
print(getattr(dog1, "age"))   # 4
setattr(dog1, "age", 10)      # same as dog1.age = 10


# ============================================================
# 2. INSTANCE vs CLASS ATTRIBUTES
# ============================================================
# Instance attribute -> defined with self.x inside __init__, separate per object.
# Class attribute    -> defined directly in the class body, SHARED by all objects.

print("\n=== 2. Instance vs Class attributes ===")


class Student:
    school = "Delhi Public School"    # class attribute (shared)
    count = 0                         # class attribute used as a counter

    def __init__(self, name, marks):
        self.name = name              # instance attribute
        self.marks = marks
        Student.count += 1            # modify the shared attribute via the class name


s1 = Student("Aman", 90)
s2 = Student("Riya", 85)

print(s1.school)          # Delhi Public School
print(Student.count)      # 2
Student.school = "KV School"
print(s2.school)          # KV School  (changed for everyone)


# ============================================================
# 3. TYPES OF METHODS
# ============================================================
# Instance method -> first param 'self'; works with the object's data.
# Class method    -> @classmethod, first param 'cls'; works with the class itself.
#                    Often used as alternative constructors.
# Static method   -> @staticmethod, no self/cls; a utility function that
#                    just lives inside the class for organisation.

print("\n=== 3. Types of methods ===")


class Person:
    species = "Homo sapiens"

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    # instance method
    def introduce(self):
        return f"Hi, I'm {self.name}"

    # class method - alternative constructor
    @classmethod
    def from_age(cls, name, age, current_year=2026):
        return cls(name, current_year - age)   # cls(...) creates a Person

    # static method - no access to self or cls
    @staticmethod
    def is_adult(age):
        return age >= 18


p = Person("Haider", 2000)
p2 = Person.from_age("Sara", 22)       # calling class method on the class
print(p.introduce())
print(p2.birth_year)                   # 2004
print(Person.is_adult(20))             # True


# ============================================================
# 4. MAGIC (DUNDER) METHODS
# ============================================================
# Special methods with double underscores. Python calls them automatically.
#   __init__   -> object creation
#   __str__    -> print(obj) / str(obj)   (human friendly)
#   __repr__   -> repr(obj)               (developer friendly / debugging)
#   __len__    -> len(obj)
#   __eq__     -> obj1 == obj2
#   __add__    -> obj1 + obj2
#   __del__    -> when object is destroyed

print("\n=== 4. Magic methods ===")


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book(title={self.title!r}, pages={self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.pages == other.pages

    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", self.pages + other.pages)


b1 = Book("Python 101", 300)
b2 = Book("OOP Basics", 150)
print(b1)                  # uses __str__
print(repr(b1))            # uses __repr__
print(len(b1))             # 300
print(b1 == b2)            # False
print(b1 + b2)             # Book: Python 101 & OOP Basics


# ============================================================
# 5. PILLAR 1 - ENCAPSULATION
# ============================================================
# Bundling data + methods together AND controlling access to that data.
# Python uses naming conventions (it has no strict private keyword):
#   name      -> public       (anyone can use)
#   _name     -> protected    (convention: "internal use, please don't touch")
#   __name    -> private      (name mangling: becomes _ClassName__name)
#
# @property lets you expose a "getter/setter" that looks like a plain attribute,
# so you can add validation without changing how the class is used.

print("\n=== 5. Encapsulation ===")


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # public
        self._bank = "SBI"            # protected (by convention)
        self.__balance = balance      # private (name-mangled)

    # getter
    @property
    def balance(self):
        return self.__balance

    # setter with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount


acc = BankAccount("Haider", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)                    # 1300 - uses the getter
acc.balance = 2000                    # uses the setter (with validation)

# print(acc.__balance)                # AttributeError - hidden by name mangling
print(acc._BankAccount__balance)      # 2000 - still reachable, but you shouldn't

try:
    acc.balance = -50
except ValueError as e:
    print("Error:", e)


# ============================================================
# 6. PILLAR 2 - INHERITANCE
# ============================================================
# A child class reuses (inherits) attributes and methods of a parent class.
#
# Syntax:  class Child(Parent):
#
# super() calls the parent's version of a method (commonly in __init__).
# Types: single, multi-level, multiple, hierarchical.

print("\n=== 6. Inheritance ===")


class Animal:                                  # parent / base / super class
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def speak(self):
        return "Some generic sound"


class Cat(Animal):                             # single inheritance
    def __init__(self, name, color):
        super().__init__(name)                 # call parent's __init__
        self.color = color                     # extra attribute only for Cat

    def speak(self):                           # method overriding
        return "Meow"


class Kitten(Cat):                             # multi-level: Animal -> Cat -> Kitten
    def play(self):
        return f"{self.name} is playing"


k = Kitten("Tom", "grey")
print(k.eat())              # inherited from Animal
print(k.speak())            # inherited from Cat (overridden)
print(k.play())             # own method
print(isinstance(k, Animal))        # True
print(issubclass(Kitten, Cat))      # True


# ----- Multiple inheritance -----
class Flyer:
    def move(self):
        return "Flying"


class Swimmer:
    def move(self):
        return "Swimming"


class Duck(Flyer, Swimmer):                    # inherits from two classes
    pass


d = Duck()
print(d.move())                                # Flying (Flyer is checked first)
print(Duck.__mro__)                            # Method Resolution Order: the lookup path


# ============================================================
# 7. PILLAR 3 - POLYMORPHISM
# ============================================================
# "Many forms": the same method name/operator behaves differently
# depending on the object it is used on.
#   a) Method overriding   (child redefines parent method)
#   b) Duck typing         ("if it quacks like a duck...") - no common parent needed
#   c) Operator overloading (via dunder methods, see section 4)

print("\n=== 7. Polymorphism ===")


# a) Method overriding
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2


shapes = [Rectangle(4, 5), Circle(3)]
for s in shapes:
    print(type(s).__name__, "area =", round(s.area(), 2))   # same call, different result


# b) Duck typing - unrelated classes, same method name
class Car:
    def start(self):
        return "Car engine started"


class Laptop:
    def start(self):
        return "Laptop booting up"


for thing in (Car(), Laptop()):
    print(thing.start())       # works as long as the object has .start()


# c) Built-in polymorphism
print(len("hello"), len([1, 2, 3]), len({"a": 1}))   # len() works on many types
print(3 + 4, "a" + "b", [1] + [2])                   # + behaves differently per type


# ============================================================
# 8. PILLAR 4 - ABSTRACTION
# ============================================================
# Hide implementation details; expose only what is necessary.
# Python does this with the 'abc' module (Abstract Base Class).
#
# - An abstract class cannot be instantiated directly.
# - @abstractmethod forces every child class to implement that method.

print("\n=== 8. Abstraction ===")

from abc import ABC, abstractmethod


class Payment(ABC):                            # abstract class
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):                             # no body - children MUST implement
        pass

    def receipt(self):                         # normal (concrete) method is allowed too
        return f"Receipt: paid {self.amount}"


class UPIPayment(Payment):
    def pay(self):
        return f"Paid {self.amount} via UPI"


class CardPayment(Payment):
    def pay(self):
        return f"Paid {self.amount} via Card"


# p = Payment(100)           # TypeError: can't instantiate abstract class

for method in (UPIPayment(500), CardPayment(1200)):
    print(method.pay())
print(UPIPayment(500).receipt())


# ============================================================
# 9. BONUS - COMPOSITION AND DATACLASSES
# ============================================================
# Composition = "has-a" relationship (a class contains objects of other classes).
# Inheritance = "is-a" relationship.  Prefer composition when it fits.

print("\n=== 9. Composition & dataclasses ===")


class Engine:
    def start(self):
        return "Engine started"


class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()                 # Vehicle HAS an Engine

    def start(self):
        return f"{self.brand}: {self.engine.start()}"


print(Vehicle("Tata").start())


# @dataclass auto-generates __init__, __repr__, __eq__ for simple data holders.
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int = 0                                 # default value


pt = Point(3, 4)
print(pt)                                      # Point(x=3, y=4)
print(pt == Point(3, 4))                       # True


# ============================================================
# QUICK REVISION
# ============================================================
# Class           -> blueprint                      class A:
# Object          -> instance of class              a = A()
# __init__        -> constructor                    def __init__(self, ...)
# self            -> the current object
# Encapsulation   -> hide data, control access      _x, __x, @property
# Inheritance     -> reuse parent's code            class B(A): / super()
# Polymorphism    -> same name, different behavior  overriding, duck typing
# Abstraction     -> hide details, show essentials  ABC + @abstractmethod