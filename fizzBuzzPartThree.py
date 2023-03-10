#Logan Limbaugh Python - FizzBuzz Part Three
# Printing FizzBuzz for numbers which are multiples of 3 and 5.

fbList = list(range(1,101))

for num in fbList:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)