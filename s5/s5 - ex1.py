input = int(input("Type a number from 1 to 10: "))

if input < 0:
    print("the input is smaller than 10.")

elif input >= 0 and input <= 10:
    print("the input is within range [0,10].")

else:
    print("the given number is greater than 10.")