class Car():

    brand = ''
    year = ''

    def __init__(self, name, color):
        self.name = name
        self.color = color


    def set_brand(self, brand):
        self.brand = brand

    def set_year(self, year):
        self.year = year

    def get_brand(self):
        return self.brand

    def get_year(self):
        return self.year

c1 = Car('Celta', 'gray')
c1.set_brand('GM')
c1.set_year(2013)

print(c1.get_brand())
print(c1.get_year())
