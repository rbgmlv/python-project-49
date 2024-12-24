import importlib
import re

import prompt

from brain_games.settings import (
    ALLOWED_ANSWERS,
    GAME_DESCRIPTION,
    ROUNDS_COUNT,
)


def load_game(game_type):
    game = importlib.import_module(f"brain_games.games.{game_type}")
    print(GAME_DESCRIPTION[game_type])
    return game


def ask_question(game):
    question, right_answer = game.define_question()
    print(f"Question: {question}")
    return right_answer


def get_answer() -> str:
    answer = prompt.string("Your answer: ")
    return answer.lower()


def is_int(text: str) -> bool:
    pattern = re.compile(r'^(|-?\d+)$')
    return pattern.match(text)


def is_allowed(user_answer) -> bool:
    if is_int(user_answer):
        return True
    if user_answer in ALLOWED_ANSWERS:
        return True
    return False


def is_correct(right_answer, user_answer) -> bool:
    if is_int(user_answer):
        return True if int(user_answer) == right_answer else False
    return True if user_answer == right_answer else False


def run_game(user_name, game_type):
    game = load_game(game_type)
    right_answers_count = 0
    while right_answers_count < ROUNDS_COUNT:
        right_answer = ask_question(game)
        user_answer = get_answer()
        if not is_allowed(user_answer):
            print("Your answer is not allowed.")
            print(f"Let's try again, {user_name}!")
            break
        if is_correct(right_answer, user_answer):
            print("Correct!")
            right_answers_count += 1
            continue
        print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{right_answer}'."
        )
        print(f"Let's try again, {user_name}!")
        break
    if right_answers_count == ROUNDS_COUNT:
        print(f"Congratulations, {user_name}!")
