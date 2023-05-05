nums = [10, -5, 0, 4, 8, -9, 34, 100]

sort = sorted(nums)
print(sort)

reversed = sorted(nums, reverse=True)
print(reversed)

names = ['Adam', 'Kevin', 'Ana', 'Joe', 'Daniel', 'Michael']
names = sorted(names)

print(names)

names = sorted(names, reverse=True)
print(names)

#Sorted function has the key parameter - we can define the logic behind sorting
#Let`s sort names based on the length of the strings

texts = ['This', 'This is a', 'T', 'This is the longest string ', 'This is the second']

def sorted_logic(x):
    return len(x)

texts = sorted(texts, key=sorted_logic)
print(texts)

texts = sorted(texts, reverse=True,key=sorted_logic)
print(texts)

#To sort dicts according to it keys
people = {'Adam Smith': 34, 'Albert Camus': 56, 'Kurt Godel': 45, 'Jean-Paul Sartre': 31}

#Sortiing by key: x[0] or by value: x[1]
def dict_sorter(x):
    return x[0]

result = sorted(people.items(), key=dict_sorter)
print(result)

#Reverse order
result = sorted(people.items(), reverse=True, key=dict_sorter)
print(result)