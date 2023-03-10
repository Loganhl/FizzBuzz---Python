#Logan Limbaugh Python - FizzBuzz Part Two
# Printing Fizz for Multiples of 3, and Buzz for Multiples of 5.

fbList = list(range(1,101))

for num in fbList:
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)