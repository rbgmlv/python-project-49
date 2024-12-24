from random import randint


def define_question():
    random_number_1 = randint(1, 30)
    random_number_2 = randint(1, 30)
    match randint(0, 2):
        case 0:
            question = str(f"{random_number_1} + {random_number_2}")
            right_answer = random_number_1 + random_number_2
        case 1:
            question = str(f"{random_number_1} - {random_number_2}")
            right_answer = random_number_1 - random_number_2
        case 2:
            question = str(f"{random_number_1} * {random_number_2}")
            right_answer = random_number_1 * random_number_2
    return question, right_answer
