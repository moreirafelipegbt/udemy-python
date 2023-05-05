#List comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Adam', 'Kevin', 'Anna', 'Joe', 'Daniel', 'Bill']

even = [num for num in numbers if num % 2 == 0]
print(even)

filtered = [name for name in names if name.startswith('A') or len(name) == 4]
print(filtered)