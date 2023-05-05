file_input = open('s10-ex1-text_file.txt', 'r')
file_output = open('s10-ex1-text_file.txt', 'a')

for line in reversed(list(file_input)):
    reversed_line = line[::-1]
    print(reversed_line)
    file_output.write(reversed_line)

file_output.close()
file_input.close()