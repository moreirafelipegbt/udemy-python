class Car:

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def show_data(self):
        return self.model

class RacingCar(Car):

    def __init__(self, model, year):
        super().__init__(model, year)

    def show_data(self):
        return "The model is {} and the year is {}".format(self.model, self.year)

c = Car('Celta', 2013)
print(c.show_data())

rc = RacingCar('Prisma', 2013)
print(rc.show_data())