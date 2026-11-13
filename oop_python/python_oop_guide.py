# ==============================================================================
# PYTHON OBJECT-ORIENTED PROGRAMMING (OOP) — COMPLETE SYNTAX & CONCEPT GUIDE
# ==============================================================================
# In this file, we cover:
#   1. Classes & Objects (How to write classes, __init__, self, creating objects)
#   2. Types of Attributes & Methods (Instance, Class, Static, Dunder/Magic)
#   3. Pillar 1: Encapsulation (Public, _Protected, __Private, @property)
#   4. Pillar 2: Inheritance (Single, super(), Overriding, Multiple, MRO)
#   5. Pillar 3: Polymorphism (Method Overriding, Duck Typing, Operator Overloading)
#   6. Pillar 4: Abstraction (Abstract Base Classes with `abc` and @abstractmethod)
#   7. Modern Python OOP Bonus: Composition ("Has-A") & @dataclass
#
# You can read this file top-to-bottom as study notes OR run it directly:
#   $ python3 python_oop_guide.py
# ==============================================================================

from abc import ABC, abstractmethod
from dataclasses import dataclass


# ==============================================================================
# SECTION 1: CLASSES & OBJECTS (THE BASICS)
# ==============================================================================
# - A CLASS is a blueprint or template (e.g., an architectural plan for a car).
# - An OBJECT (or instance) is a concrete item built from that blueprint.
# - `self` refers to the specific object being created or acted upon.
# - `__init__` is the constructor method that runs automatically when you
#   create a new object to initialize its data (attributes).
# ==============================================================================

class Car:
    # CLASS ATTRIBUTE: Shared across ALL instances of the Car class.
    wheels = 4
    total_cars_created = 0

    def __init__(self, brand: str, model: str, year: int):
        """
        Constructor (__init__): Initializes instance attributes unique to each object.
        `self` binds the attributes to the specific object being created.
        """
        self.brand = brand          # Instance attribute
        self.model = model          # Instance attribute
        self.year = year            # Instance attribute
        self.is_running = False     # Default instance attribute

        # Increment the shared class attribute whenever a new Car is created
        Car.total_cars_created += 1

    # INSTANCE METHOD: Operates on a specific object using `self`.
    def start_engine(self) -> str:
        self.is_running = True
        return f"The {self.year} {self.brand} {self.model}'s engine is now running."

    def stop_engine(self) -> str:
        self.is_running = False
        return f"The {self.year} {self.brand} {self.model}'s engine is now off."

    # CLASS METHOD: Receives the class (`cls`) instead of `self`.
    # Commonly used to access class-level state or create "alternative constructors".
    @classmethod
    def from_dash_string(cls, car_str: str) -> "Car":
        """Alternative constructor that creates a Car from 'Brand-Model-Year'."""
        brand, model, year_str = car_str.split("-")
        return cls(brand, model, int(year_str))

    # STATIC METHOD: Does not receive `self` or `cls`.
    # Acts like a regular utility function that logically belongs inside the class.
    @staticmethod
    def is_vintage(year: int) -> bool:
        """Returns True if a car model year is 25+ years old (relative to 2026)."""
        return (2026 - year) >= 25

    # DUNDER (DOUBLE UNDERSCORE) / MAGIC METHODS:
    # Customize how built-in Python operations (`print()`, `repr()`, `==`) work.
    def __str__(self) -> str:
        """User-friendly string representation used by print() and str()."""
        status = "Running" if self.is_running else "Parked"
        return f"{self.year} {self.brand} {self.model} [{status}]"

    def __repr__(self) -> str:
        """Developer-facing representation used in debuggers and interactive shells."""
        return f"Car(brand={self.brand!r}, model={self.model!r}, year={self.year!r})"


# ==============================================================================
# SECTION 2: PILLAR 1 — ENCAPSULATION
# ==============================================================================
# Concept:
#   Bundling data (attributes) and methods that operate on that data into a
#   single unit (class), while restricting direct unauthorized access to
#   sensitive internal state.
#
# Access Modifiers in Python (by naming convention):
#   1. Public    (`self.owner`)    : Accessible from anywhere.
#   2. Protected (`self._type`)    : Single underscore `_`. Convention telling
#                                    other developers: "Internal use or subclasses only."
#   3. Private   (`self.__balance`): Double underscore `__`. Triggers Python's
#                                    "name mangling" (`_ClassName__balance`) so it
#                                    cannot be accidentally overwritten or accessed directly.
#
# Pythonic Getters & Setters:
#   Instead of writing Java-style `get_balance()` and `set_balance()`, Python uses
#   the `@property` decorator so you can access a method like a normal attribute
#   while still running validation logic under the hood.
# ==============================================================================

class BankAccount:
    def __init__(self, owner: str, initial_balance: float, account_type: str = "Savings"):
        self.owner = owner                  # Public attribute
        self._account_type = account_type   # Protected attribute (single underscore)
        self.__balance = 0.0                # Private attribute (double underscore)

        # Use our validated setter right in the constructor
        self.balance = initial_balance

    # GETTER using @property
    @property
    def balance(self) -> float:
        """Allows reading `account.balance` safely without exposing `__balance` directly."""
        return self.__balance

    # SETTER using @<property_name>.setter
    @balance.setter
    def balance(self, amount: float) -> None:
        """Validates data before allowing `__balance` to be updated."""
        if amount < 0:
            raise ValueError("Account balance cannot be negative!")
        self.__balance = float(amount)

    def deposit(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"

    def withdraw(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount
        return f"Withdrew ${amount:.2f}. Remaining balance: ${self.__balance:.2f}"


# ==============================================================================
# SECTION 3: PILLAR 2 — INHERITANCE
# ==============================================================================
# Concept:
#   Allows a new class (Child / Subclass / Derived class) to inherit attributes
#   and methods from an existing class (Parent / Superclass / Base class).
#   Models an "IS-A" relationship (e.g., a Developer IS AN Employee).
#
# Key Syntax:
#   - `class ChildClass(ParentClass):`
#   - `super().__init__(...)` calls the parent class's constructor so you don't
#     repeat initialization code.
#   - Method Overriding: Redefining a parent method in the child class to give
#     it specialized behavior.
#   - Multiple Inheritance: `class Hybrid(ParentA, ParentB):` — resolved using
#     Python's Method Resolution Order (`ClassName.mro()`).
# ==============================================================================

class Employee:
    """Parent (Base) Class"""
    def __init__(self, name: str, emp_id: int, base_salary: float):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_pay(self) -> float:
        return self.base_salary

    def get_role_summary(self) -> str:
        return f"Employee #{self.emp_id}: {self.name}"


class Developer(Employee):
    """Child (Derived) Class inheriting from Employee"""
    def __init__(self, name: str, emp_id: int, base_salary: float, programming_language: str, bonus: float):
        # Call the Parent class constructor using super()
        super().__init__(name, emp_id, base_salary)
        # Add child-specific attributes
        self.programming_language = programming_language
        self.bonus = bonus

    # METHOD OVERRIDING: Customizing how pay is calculated for a Developer
    def calculate_pay(self) -> float:
        parent_pay = super().calculate_pay()
        return parent_pay + self.bonus

    # METHOD OVERRIDING: Extending parent summary
    def get_role_summary(self) -> str:
        return f"{super().get_role_summary()} | Role: {self.programming_language} Developer"


class Manager(Employee):
    """Another Child Class inheriting from Employee"""
    def __init__(self, name: str, emp_id: int, base_salary: float, team_size: int):
        super().__init__(name, emp_id, base_salary)
        self.team_size = team_size

    def calculate_pay(self) -> float:
        # Managers receive $500 extra per team member managed
        return super().calculate_pay() + (self.team_size * 500.0)

    def get_role_summary(self) -> str:
        return f"{super().get_role_summary()} | Role: Manager (Team of {self.team_size})"


# --- Multiple Inheritance Example ---
class Flyable:
    def fly(self) -> str:
        return "Flying through the air!"


class Swimmable:
    def swim(self) -> str:
        return "Swimming in the water!"


class Duck(Flyable, Swimmable):
    """Inherits capabilities from BOTH Flyable and Swimmable."""
    def sound(self) -> str:
        return "Quack!"


# ==============================================================================
# SECTION 4: PILLAR 3 — POLYMORPHISM
# ==============================================================================
# Concept:
#   "Poly" (many) + "Morph" (forms). It means the SAME method name, interface,
#   or operator can behave differently depending on the object calling it.
#
# 3 Ways Polymorphism Works in Python:
#   1. Subtype Polymorphism (Method Overriding):
#      Calling `.calculate_pay()` on a list of mixed `Employee`, `Developer`,
#      and `Manager` objects—each executes its own version automatically.
#   2. Duck Typing ("If it walks like a duck and quacks like a duck..."):
#      Python doesn't require classes to share a parent class to be treated
#      polymorphically—they just need to implement the same method name.
#   3. Operator Overloading:
#      Giving custom meaning to standard operators like `+`, `==`, `<` via
#      dunder methods (`__add__`, `__eq__`, `__lt__`).
# ==============================================================================

# --- 1. Duck Typing Example (Unrelated classes sharing the same method name) ---
class EmailNotifier:
    def send(self, message: str) -> str:
        return f"[EMAIL SENT]: {message}"


class SMSNotifier:
    def send(self, message: str) -> str:
        return f"[SMS SENT]: {message}"


class PushNotifier:
    def send(self, message: str) -> str:
        return f"[PUSH NOTIFICATION]: {message}"


def broadcast_alert(notifiers: list, alert_text: str) -> list[str]:
    """
    Polymorphic function: Doesn't care about the exact class type of `notifier`,
    as long as it has a `.send(message)` method!
    """
    return [notifier.send(alert_text) for notifier in notifiers]


# --- 2. Operator Overloading Example (`+` and `==` on custom objects) ---
class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        """Overloads the `+` operator so `v1 + v2` adds their coordinates."""
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        """Overloads the `==` operator to compare values instead of memory addresses."""
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"


# ==============================================================================
# SECTION 5: PILLAR 4 — ABSTRACTION
# ==============================================================================
# Concept:
#   Hiding complex internal implementation details and showing only the essential
#   interface (what an object does, not how it does it).
#   In OOP, we enforce this using Abstract Base Classes (ABCs):
#   - An Abstract Class CANNOT be instantiated directly (`PaymentGateway()` fails).
#   - Any method decorated with `@abstractmethod` is a strict contract: every
#     child class MUST implement that method, or Python raises a `TypeError`
#     when you try to create an object of that child class.
# ==============================================================================

class PaymentGateway(ABC):
    """
    Abstract Base Class defining the strict blueprint for all payment processors.
    """
    def __init__(self, merchant_id: str):
        self.merchant_id = merchant_id

    # Concrete method (shared helper available to all subclasses)
    def format_receipt(self, amount: float, tx_id: str) -> str:
        return f"Receipt [Merchant: {self.merchant_id} | Tx: {tx_id} | Amount: ${amount:.2f}]"

    # ABSTRACT METHODS: Subclasses are FORCED to implement these!
    @abstractmethod
    def authenticate(self) -> bool:
        """Verify API credentials with the payment provider."""
        pass

    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """Execute the charge and return a formatted receipt."""
        pass


class StripeGateway(PaymentGateway):
    """Concrete implementation of PaymentGateway for Stripe."""
    def __init__(self, merchant_id: str, api_key: str):
        super().__init__(merchant_id)
        self.__api_key = api_key

    def authenticate(self) -> bool:
        # Simulated API key check
        return self.__api_key.startswith("sk_live_")

    def process_payment(self, amount: float) -> str:
        if not self.authenticate():
            raise PermissionError("Invalid Stripe API Key!")
        # Internal Stripe-specific complexity is hidden from the caller
        tx_id = "stripe_tx_9012"
        return self.format_receipt(amount, tx_id)


class UPIPaymentGateway(PaymentGateway):
    """Concrete implementation of PaymentGateway for UPI."""
    def __init__(self, merchant_id: str, vpa_id: str):
        super().__init__(merchant_id)
        self.vpa_id = vpa_id

    def authenticate(self) -> bool:
        return "@" in self.vpa_id

    def process_payment(self, amount: float) -> str:
        if not self.authenticate():
            raise PermissionError("Invalid UPI VPA handle!")
        tx_id = "upi_tx_4481"
        return self.format_receipt(amount, tx_id)


# ==============================================================================
# SECTION 6: MODERN PYTHON OOP BONUS — COMPOSITION & @dataclass
# ==============================================================================
# 1. Composition ("HAS-A" relationship):
#    Instead of deep inheritance trees, build complex objects out of smaller
#    component objects (e.g., a Computer HAS-A CPU).
# 2. `@dataclass`:
#    Automatically generates `__init__`, `__repr__`, and `__eq__` for classes
#    that primarily store data.
# ==============================================================================

@dataclass
class CPU:
    model: str
    cores: int

    def execute(self) -> str:
        return f"CPU ({self.model}, {self.cores} cores) is executing instructions."


class Laptop:
    """Demonstrates Composition: Laptop HAS-A CPU object inside it."""
    def __init__(self, brand: str, cpu: CPU):
        self.brand = brand
        self.cpu = cpu  # Composed object

    def boot_up(self) -> str:
        return f"Booting {self.brand} laptop -> {self.cpu.execute()}"


# ==============================================================================
# INTERACTIVE DEMONSTRATION (RUN THIS FILE TO SEE OUTPUT)
# ==============================================================================

if __name__ == "__main__":
    print("=" * 72)
    print("1. CLASSES & OBJECTS IN ACTION")
    print("=" * 72)
    # Creating (instantiating) objects from the Car class
    car1 = Car("Toyota", "Camry", 2024)
    car2 = Car.from_dash_string("Ford-Mustang-1969")  # Using @classmethod constructor

    print("Object 1 (str)       :", car1)
    print("Object 2 (repr)      :", repr(car2))
    print("Calling method       :", car1.start_engine())
    print("Updated state        :", car1)
    print("Shared class attr    : Wheels =", Car.wheels, "| Total Cars =", Car.total_cars_created)
    print("Static method check  : Is 1969 vintage?", Car.is_vintage(car2.year))

    print("\n" + "=" * 72)
    print("2. PILLAR 1: ENCAPSULATION IN ACTION")
    print("=" * 72)
    acct = BankAccount(owner="Aarav", initial_balance=1000.0)
    print(acct.deposit(500.0))
    print(acct.withdraw(200.0))
    print("Reading via @property:", f"${acct.balance:.2f}")

    # Trying to set an invalid negative balance triggers our @balance.setter validation
    try:
        acct.balance = -50.0
    except ValueError as err:
        print("Setter validation    : Caught expected error ->", err)

    print("\n" + "=" * 72)
    print("3. PILLAR 2: INHERITANCE IN ACTION")
    print("=" * 72)
    dev = Developer(name="Priya", emp_id=101, base_salary=80000, programming_language="Python", bonus=12000)
    mgr = Manager(name="Rohan", emp_id=102, base_salary=90000, team_size=8)

    print(dev.get_role_summary(), "-> Pay: $", dev.calculate_pay())
    print(mgr.get_role_summary(), "-> Pay: $", mgr.calculate_pay())

    donald = Duck()
    print("Multiple Inheritance :", donald.fly(), "|", donald.swim(), "|", donald.sound())
    print("Duck MRO             :", [cls.__name__ for cls in Duck.mro()])

    print("\n" + "=" * 72)
    print("4. PILLAR 3: POLYMORPHISM IN ACTION")
    print("=" * 72)
    # Subtype Polymorphism: Same method call `.calculate_pay()` on different employee types
    staff: list[Employee] = [
        Employee("Sam", 100, 50000),
        dev,
        mgr,
    ]
    for member in staff:
        print(f"Polymorphic Pay Call -> {member.name}: ${member.calculate_pay():.2f}")

    # Duck Typing Polymorphism
    channels = [EmailNotifier(), SMSNotifier(), PushNotifier()]
    for output in broadcast_alert(channels, "Server maintenance at 10 PM"):
        print("Duck Typing          ->", output)

    # Operator Overloading Polymorphism
    v1 = Vector2D(2, 5)
    v2 = Vector2D(4, -1)
    print("Operator Overloading ->", f"{v1} + {v2} = {v1 + v2}")

    print("\n" + "=" * 72)
    print("5. PILLAR 4: ABSTRACTION IN ACTION")
    print("=" * 72)
    # Trying to instantiate the abstract class directly fails:
    try:
        bad_gateway = PaymentGateway("MERCH_01")  # type: ignore[abstract]
    except TypeError as err:
        print("Abstract safeguard   : Cannot instantiate ABC directly ->", err)

    # Concrete subclasses work seamlessly through the unified interface:
    gateways: list[PaymentGateway] = [
        StripeGateway(merchant_id="STORE_99", api_key="sk_live_abc123"),
        UPIPaymentGateway(merchant_id="STORE_99", vpa_id="shop@okaxis"),
    ]
    for gw in gateways:
        print("Abstract Contract    ->", gw.process_payment(149.99))

    print("\n" + "=" * 72)
    print("6. BONUS: COMPOSITION & @dataclass IN ACTION")
    print("=" * 72)
    chip = CPU(model="Apple M4 Pro", cores=14)
    my_laptop = Laptop(brand="MacBook Pro", cpu=chip)
    print("Dataclass repr       :", chip)
    print("Composition ('Has-A'):", my_laptop.boot_up())
    print("=" * 72)