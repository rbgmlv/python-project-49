from random import randint

from brain_games.constants import PROGRESSION_LENGTH

GAME_RULE = 'What number is missing in the progression?'


def define_question():
    first_element = randint(0, 30)
    step = randint(2, 10)
    progression = []
    element = first_element
    question = ''
    for i in range(0, PROGRESSION_LENGTH):
        progression.append(element)
        element += step
    random_index = randint(0, PROGRESSION_LENGTH - 1)
    right_answer = progression[random_index]
    progression[random_index] = '..'
    for i in range(0, PROGRESSION_LENGTH):
        question += str(progression[i]) + ' '
    question.strip()
    return question, str(right_answer)
