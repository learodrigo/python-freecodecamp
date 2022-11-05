def palindrome():
    text = input(f"Lemme check if this is a palindrome: ")
    inverted = text[::-1]
    if text == inverted:
        print(f"{text} is a palindrome")
    else:
        print(f"This is not")


if __name__ == "__main__":
    palindrome()
