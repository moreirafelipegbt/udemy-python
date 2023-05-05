names = ['Adam', 'Daniel', 'Ana']
ages = [34, 12, 54]

dict = {}

for key, value in zip(names, ages):
    dict[key] = value

print(dict)