class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name+' says Woof'


class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name+' says Meow'


niko = Dog('Nigo')
felix = Cat('Felix')
print(niko.speak())
print(felix)


#base class
class Car:
    def __init__(self, br, ve):
        self.brand = br
        self.velocity = ve

    def __str__(self):
        return f"The {self.brand} drives at {self.velocity:,} km/h"

    def accelerate(self,value):
        self.velocity += value

#child class
class Limo(Car):
    def __init__(self, br, ve,pa):
        Car.__init__(self,br,ve)
        self.passenger = pa
    def __str__(self):
        return Car. __str__(self) + " with " \
               + str(self.passenger)+  " passenger"
    def enter(self,number):
        self.passenger +=number
    def exit(self,number):
        self.passenger -=number


class Truck(Car):
    def __init__(self,br,ve, la):
        Car.__init__(self,br,ve)
        self.last = la
    def __str__(self):
        return Car.__str__(self) + " with  " \
               +str(self.last) + " tones last"
    def load(self,value):
        self.last +=value
    def unload(self,value):
        self.last -=value

class DeliveryTruck(Limo,Truck):
    def __init__(self,br,ve,pa,la):
        Limo.__init__(self,br,ve,pa)
        Truck. __init__(self,br,ve,la)
    def __str__(self):
        return Limo.__str__(self) + "\n" \
               + Truck.__str__(self)

#testen
toyota = DeliveryTruck("Allround",40,2,3.5)
#code hier
print(toyota)