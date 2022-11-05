def acronnyms():
    text = input(f"Write some text and I'll write the acronym: ")
    words = text.split(" ")
    acronnym = ""

    for word in words:
        if word[0].upper() == word[0]:
            acronnym += word[0].upper()

    if len(acronnym) > 0:
        print(f"Your acronym is {acronnym}")


if __name__ == "__main__":
    acronnyms()
