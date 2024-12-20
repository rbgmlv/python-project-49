from random import randint

import prompt

import brain_games.settings


def describe_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_answer() -> str:
    question = randint(1, 100)
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return question, answer


def is_even(num: int) -> bool:
    return True if num % 2 == 0 else False


def is_allowed(answer: str) -> bool:
    allowed_answers = brain_games.settings.allowed_answers
    if answer.lower() in allowed_answers:
        return True
    return False


def is_yes(answer: str) -> bool:
    if is_allowed(answer):
        if answer.lower() == 'yes':
            return True
        if answer.lower() == 'no':
            return False


def is_correct(question: int, answer: str) -> bool:
    if is_allowed(answer):
        if is_even(question) == is_yes(answer):
            return True
        return False


def run_game(user_name):
    right_answers_count = 0
    comments = brain_games.settings.comments
    describe_game()
    while right_answers_count < 3:
        question, answer = get_answer()
        if not is_allowed(answer):
            print(comments['not_allowed_answer'])
            print(f"Let's try again, {user_name}!")
            break
        if is_correct(question, answer):
            print(comments['correct_answer'])
            right_answers_count += 1
            continue
        if is_yes(answer):
            print(comments['yes_answer'])
            print(f"Let's try again, {user_name}!")
            break
        print(comments['no_answer'])
        print(f"Let's try again, {user_name}!")
        break
    if right_answers_count == 3:
        print(f'Congratulations, {user_name}!')
    return None
