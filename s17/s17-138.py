nums = [1,2,3,4,5,6,7,8,9,10]

#Print the even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, nums))
print(even_numbers)

#Print the odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, nums))
print(odd_numbers)

names = ['Adam', 'Ana', 'Kevin', 'Daniel', 'Michael']

#Filter the names that have more than 5 characters od length

filtered_names = list(filter(lambda name: len(name) > 5, names))

print(filtered_names)