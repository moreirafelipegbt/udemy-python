class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class FacebookUser(User):

    def __init__(self, name, age):
        super().__init__(name, age)

u = User('Felipe', 32)
print(u.name)

fu = FacebookUser('Djalma', 31)
print(fu.name)