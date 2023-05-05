names = ['Adam', 'Kevin', 'Joe']
nums = [1, 2, 1]

capitalized = list(map(lambda name, number: name.capitalize() * number, names, nums))

print(capitalized)