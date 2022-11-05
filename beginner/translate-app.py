# Giraffe Language
# vowels -> g
# -----------
# dog -> dgg
# cat -> cgt


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation += "G" if letter.isupper() else "g"
        else:
            translation += letter
    return translation


input_phrase = input("Insert a phrase to be translated to Giraffe: ")

print(translate(input_phrase))
