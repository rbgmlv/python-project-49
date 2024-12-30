import prompt

from brain_games.constants import (
    GAME_DESCRIPTION,
    ROUNDS_COUNT,
)


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def run_game(game):
    user_name = welcome_user()
    game_type = game.__name__.split('.')[-1]
    print(GAME_DESCRIPTION[game_type])
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
            f"Correct answer was '{right_answer}'."
        )
        print(f"Let's try again, {user_name}!")
        return right_answers_count
    if right_answers_count == ROUNDS_COUNT:
        print(f"Congratulations, {user_name}!")
