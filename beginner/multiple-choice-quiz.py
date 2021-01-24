from Question import Question

questions_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Red/Green\n(b) Orange\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Purple\n(b) Red\n(c) Orange\n\n"
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "c"),
    Question(questions_prompts[2], "b"),
]

def run_test(questions):
    score = 0

    for q in questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 100
    print("You got", str(int(score / 100)), "/", str(len(questions)))

    return score


print("You got", run_test(questions), "points.")

