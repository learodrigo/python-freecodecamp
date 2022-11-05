def tip_calculator():
    print("How much did you spend in total? ")
    text = input(f"")

    try:
        number: float = float(text)
    except ValueError:
        print("Invalid format")
        return

    print("How much tip would like to give?")
    print("a. 18")
    print("b. 20")
    print("c. 25")

    text = input(f"")

    try:
        if text == "a" or text == "A":
            percentage = 18
        elif text == "b" or text == "B":
            percentage = 20
        elif text == "c" or text == "C":
            percentage = 25
    except ValueError:
        print("Incorrect answer")
        return

    tip = (percentage * number) / 100
    print(
        f"{percentage}% tip is ${tip:.2f}, which brings your total to ${(tip + number):.2f}"
    )


if __name__ == "__main__":
    tip_calculator()
