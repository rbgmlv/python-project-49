from random import randint


def is_even(num: int) -> bool:
    return True if num % 2 == 0 else False


def define_question():
    random_number = randint(1, 100)
    question = str(random_number)
    if is_even(random_number):
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer
