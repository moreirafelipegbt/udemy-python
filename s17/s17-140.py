from functools import reduce

original_values = [1, 2, 3, 4, 5]
#sum up the values

summary = reduce(lambda x, y: x + y, original_values)
print(summary)

#Multiply the values
multiplied = reduce(lambda x, y: x * y, original_values)
print(multiplied)

names = ['Adam', 'Ana', 'Kevin', 'Daniel', 'Michael']

#Given the list of names above, concatenate the names
concatenaded = reduce(lambda name1, name2: name1[0] + name2[0], names)
print(concatenaded)

values = [1, -5, 10, 450, 23, 99, -34]
#given the list above, calculate the min and max values
min = reduce(lambda x, y: x if x < y else y, values)
print(min)

max = reduce(lambda x, y: x if x > y else y, values)
print(max)