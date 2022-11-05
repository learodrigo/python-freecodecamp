import random
import string
from words import words


def get_valid_word(arr):
    word = random.choice(arr)

    while "-" in word or " " in word:
        word = random.choice(arr)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(
            f"You have {lives} left, and have used these letters: ",
            " ".join(used_letters),
        )

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Choose a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                lives += 0.5
                print("Well Done!")

            else:
                lives -= 1
                print("Letter isn't in the word")

        elif user_letter in used_letters:
            print("You have used that letter already.")

        else:
            print("That's not correct. Try again")

    if lives == 0:
        print("You're dead, maybe next time! The word was", word)
    else:
        print("YAY! You guessed the word", word, "!")


hangman()
