import prompt
import random


def expressions():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    print('What is the result of the expression?')

    count = 0
    while count < 3:
        operation_random = random.choice(('+', '-', '*'))
        number_random_1 = random.randint(1, 10)
        number_random_2 = random.randint(1, 10)
        question = f'{number_random_1} {operation_random} {number_random_2}'
        print(question)
        if operation_random == '+':
            question_addition = number_random_1 + number_random_2
            answer = prompt.integer('Your answer: ')
            if answer != question_addition:
                print(f"{answer} is wrong answer ;(. "
                      f"Correct answer was {answer}.")
                print(f"Let's try again, {name}!")
                break
            else:
                print('Correct')
                count += 1

        elif operation_random == '-':
            question_subtraction = number_random_1 - number_random_2
            answer = prompt.integer('Your answer: ')
            if answer != question_subtraction:
                print(f"{answer} is wrong answer ;(. "
                      f"Correct answer was {answer}.")
                print(f"Let's try again, {name}!")
                break
            else:
                print('Correct')
                count += 1

        else:
            question_multiplication = number_random_1 * number_random_2
            answer = prompt.integer('Your answer: ')
            if answer != question_multiplication:
                print(f"{answer} is wrong answer ;(. "
                      f"Correct answer was {answer}.")
                print(f"Let's try again, {name}!")
                break
            else:
                print('Correct')
                count += 1
    else:
        print(f'Congratulations, {name}')
