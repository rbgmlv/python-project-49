import math
from random import randint


def define_question():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    question = str(f"{random_number_1} {random_number_2}")
    right_answer = math.gcd(random_number_1, random_number_2)
    return question, right_answer
