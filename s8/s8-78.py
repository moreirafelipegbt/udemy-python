class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

p1 = Person('Felipe', 32)
p2 = Person('Felipe', 32)

print(p1 == p2)