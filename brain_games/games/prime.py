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
    question = randint(1, 1000)
    right_answer = "yes" if is_prime(question) else "no"
    return str(question), right_answer
