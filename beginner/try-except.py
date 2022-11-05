def check_input_number():
    is_valid = True

    while is_valid:
        try:
            number = int(input("Enter a number: "))
            is_valid = False
            print(number)
        except:
            print("Invalid input, try again")


def check_user_input():
    is_valid = True

    while is_valid:
        try:
            value = 10 / 0
            number = int(input("Enter a number: "))
            is_valid = False
            print(number)
        except ZeroDivisionError as err:
            print(err)
        except ValueError as err:
            print(err)


check_user_input()
