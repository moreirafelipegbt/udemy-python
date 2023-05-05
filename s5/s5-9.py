name = 'Felipe Moreira '
age = 32
weight = 83

text = "This is just a text from a {} guy with {} of weight."

slicer = name[0:3]
slicer = name[1:3]
print(slicer)

result = text.format(age, weight)
print(result)