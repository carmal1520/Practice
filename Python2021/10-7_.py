
while True:

    try:    
        number1 = input("Give me a number: ")

        number2 = input("Give me another number: ")

        sum = int(number1) + int(number2)

    except ValueError:
        print("You can only use numbers")
    else:
        print(f"The sum of the two numbers are {sum}")