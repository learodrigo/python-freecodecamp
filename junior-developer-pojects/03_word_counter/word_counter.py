def word_counter():
    text = input(f"Write something: ")
    words = text.split(" ")
    print(f"You wrote {len(words)} words")


if __name__ == "__main__":
    word_counter()
