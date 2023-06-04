class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

    def __le__(self, other):
        if(self.age<other.age):
            return self
        else:
            return other

Sakib = Cricketer('Sakib', 38, 68, 91)
Mushfiq = Cricketer('Mushfiq', 36, 55, 82)
Mustafiz = Cricketer('Mustafiz', 27, 69, 86)
Riyad = Cricketer('Riyad', 39, 72, 92)

com1 = Cricketer.__le__(Sakib, Mushfiq)
com2 = Cricketer.__le__(Mustafiz, Riyad)
final = Cricketer.__le__(com1, com2)

print(final.name)