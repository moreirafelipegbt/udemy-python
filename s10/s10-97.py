try:

    #Using with it isn't necessary to close the file
    with open('text_fil.txt', 'r') as file:
        for line in file:
            print(line)

except FileNotFoundError as error:
    print('Couldn\'t find the file. Error message: {}'.format(error.args[1]))