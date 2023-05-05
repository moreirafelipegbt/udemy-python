#== compares values
#'is' compares memory location

a = [83, 'String', True, 55.5]
b = [83, 'String', True, 55.5]

print(a == b)
print(a is b)

b = a
print(a == b)
print(a is b)
