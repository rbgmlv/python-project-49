from random import randint


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    stack = []
    x = 1
    while x <= num:
        if num % x == 0:
            stack.append(x)
        if len(stack) > 2:
            break
        x += 1
    return True if len(stack) < 3 else False


def define_question():
    random_number = randint(1, 1000)
    question = str(random_number)
    if is_prime(random_number):
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer
