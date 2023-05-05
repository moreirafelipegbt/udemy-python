class Vehicle:

    def __init__(self, brand, year, eficienty):
        self.brand = brand
        self.year = year
        self.eficienty = eficienty

    def calculate_consuption(self, km):
        pass


class Bus(Vehicle):

    def __init__(self, brand, year, efitienty = 11):
        super().__init__(self, brand, year)
        self.eficienty = efitienty

    def calculate_consuption(self, km):
        return "The consuption for car is: {}".format(km * self.eficienty)

class Car(Vehicle):

    def __init__(self, brand, year, efitienty = 12):
        super().__init__(self, brand, year)
        self.eficienty = efitienty

    def calculate_consuption(self, km):
        return "The consuption for bus is: {}".format(km * self.eficienty)

b = Bus('VolksWagen', 2022)
c = Car('GM', 2023)

print(b.calculate_consuption(2))
print(c.calculate_consuption(3))