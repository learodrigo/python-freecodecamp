import random


def play():
    user = input("Select your move!\n(R) Rock\n(P) Paper\n(S) Scissors\n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won!"

    return "You lost"


def is_win(player, opponent):
    # returns true if player wins
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


print(play())
