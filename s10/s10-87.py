#Count the occurrence of word 'is' in lowercase

file = open('text_file.txt', 'r')

word_occurrence = 0

for line in file:
    words = line.split()
    word_occurrence += len([word for word in words if word.lower() == 'is'])

print(word_occurrence)
file.close()