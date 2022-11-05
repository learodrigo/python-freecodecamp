def odd_or_even():
    accessed = input(f"Select a number: ")

    try:
        number = int(accessed)
    except ValueError:
        print("Invalid number")
        return

    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


if __name__ == "__main__":
    odd_or_even()
