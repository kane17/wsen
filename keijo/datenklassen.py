from dataclasses import dataclass
import math, typing

@dataclass

class Vektor:
    x: float = 0.0
    y: typing.Any = 0.0

    def betrag(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

vektor1 = Vektor(3.0, 4.0)
vektor2 = Vektor(3.0, 4.5)
print(vektor1 == vektor2)

@dataclass
class Person:
    name: str
    alter: str
    def display(self):
        return f"Name: {self.name}, Alter: {self.alter}"

p1 = Person("erling", "20")
print(p1.display())

