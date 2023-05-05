class Person():
    def __init__(self, name, age = 32):
        self.name = name
        self.age = age

    def show_name(self):
        print("My name is " + self.name + ". I'm " + str(self.age) + " years old.")

p2 = Person("Felipe")
print(p2.show_name())