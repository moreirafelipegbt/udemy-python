file = open('text_file.txt', 'r')
lines_counter = 0
words_counter = 0

for line in file:
    words = line.split()

    words_counter += len(words)
    lines_counter += 1

print(lines_counter)
print(words_counter)
file.close()