import prompt

from brain_games.constants import (
    ROUNDS_COUNT,
)


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run_game(game):
    user_name = welcome_user()
    print(game.GAME_RULE)
    right_answers_count = 0
    while right_answers_count < ROUNDS_COUNT:
        question, right_answer = game.define_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").lower()
        if user_answer == right_answer:
            print("Correct!")
            right_answers_count += 1
            continue
        print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{right_answer}'.\n"
            f"Let's try again, {user_name}!"
        )
        return right_answers_count
    print(f"Congratulations, {user_name}!")
