class Person:

    __color = 'Green'

    def get_color(self):
        print(self.__color)

p1 = Person()
#p1.get_color() Doesn't work because it's private

print(p1._Person__color)