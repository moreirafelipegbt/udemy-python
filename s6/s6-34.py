def returns(n):
    for number in range(n):
        if n % 2 == 0:
            return n
def yields(n):
    for number in range(n):
        if n % 2 == 0:
            yield n

returns(10)

for item in yields(10):
    print(item)