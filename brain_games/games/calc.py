from random import randint

GAME_RULE = 'What is the result of the expression?'


def define_question():
    random_number_1 = randint(1, 30)
    random_number_2 = randint(1, 30)
    random_case = randint(0, 2)
    match random_case:
        case 0:
            question = f"{random_number_1} + {random_number_2}"
            right_answer = random_number_1 + random_number_2
        case 1:
            question = f"{random_number_1} - {random_number_2}"
            right_answer = random_number_1 - random_number_2
        case 2:
            question = f"{random_number_1} * {random_number_2}"
            right_answer = random_number_1 * random_number_2
    return str(question), str(right_answer)
