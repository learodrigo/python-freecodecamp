import random


def guess(x):
    random_number = random.randint(1, x)

    assump_num = 0

    while assump_num != random_number:
        assump_num = int(input(f"Guess a number between 1 and {x}: "))

        if assump_num < random_number:
            print("Sorry, that's too low")
        elif assump_num > random_number:
            print("Now it's too high :/")

    print()
    print("-----------------------------------------------------")
    print(f"Congrats! You did it. {assump_num} was the correct number")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            assump_num = random.randint(low, high)
        else:
            assump_num = low

        feedback = input(f"Is {assump_num} too high (H), too low (L) or correct (C)?").lower()
        if feedback == 'h':
            high = assump_num - 1
        elif feedback == 'l':
            low = assump_num + 1

    print(f"Yay, the computer guess your number {assump_num}")


# guess(20)
computer_guess(20)
