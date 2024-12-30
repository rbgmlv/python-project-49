from random import randint


def is_even(num: int) -> bool:
    return True if num % 2 == 0 else False


def define_question():
    question = randint(1, 100)
    right_answer = "yes" if is_even(question) else "no"
    return str(question), right_answer
