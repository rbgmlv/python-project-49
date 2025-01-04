import math
from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def define_question():
    question = randint(1, 1000)
    right_answer = "yes" if is_prime(question) else "no"
    return str(question), right_answer
