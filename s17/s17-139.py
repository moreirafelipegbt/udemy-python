nums = [1,2,3,4,5,6,7,8,9,10]

#Print a list of doubled numbers
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

#Print a list of numbers elevated to square
squared = list(map(lambda x: x * x, nums))
print(squared)


names = ['Adam', 'Ana', 'Kevin', 'Daniel', 'Michael']

#Print a list that returns the length of each name
lengths = list(map(lambda name: len(name), names))
print(lengths)

sub_numbers1 = [1,2,3,4,5]
sub_numbers2 = [6,7,8,9,10]

#Given the lists above, return the sum bv numbers of both
summary = list(map(lambda x, y: x + y, sub_numbers1, sub_numbers2))
print(summary)