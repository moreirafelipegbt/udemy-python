#Practice multiple returns
def operation(x):
    if x % 2 == 0:
        return True, 1, "This is even"

    return False, 0, "This is odd"

b, v, s = operation(10)
print(b,v,s)

a, b, c = operation(11)
print(a,b,c)