import prompt
import random


def input_messages(mes_1, mes_2, mes_3):
    print(f'"{mes_1}" is wrong answer ;(. '
          f'Correct answer was "{mes_2}".')
    print(f'Let\'s try again, {mes_3}!')


def expressions():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')

    count = 0
    while count < 3:
        operation_random = random.choice(('+', '-', '*'))
        number_random_1 = random.randint(1, 10)
        number_random_2 = random.randint(1, 10)

        question = f'{number_random_1} {operation_random} {number_random_2}'
        print(question)

        match operation_random:
            case '+':
                question_addition = number_random_1 + number_random_2
                answer = prompt.integer('Your answer: ')
                if answer != question_addition:
                    input_messages(answer, question_addition, name)
                    break
                else:
                    print('Correct')
                    count += 1

            case '-':
                question_subtraction = number_random_1 - number_random_2
                answer = prompt.integer('Your answer: ')
                if answer != question_subtraction:
                    input_messages(answer, question_subtraction, name)
                    break
                else:
                    print('Correct')
                    count += 1

            case _:
                question_multiplication = number_random_1 * number_random_2
                answer = prompt.integer('Your answer: ')
                if answer != question_multiplication:
                    input_messages(answer, question_multiplication, name)
                    break
                else:
                    print('Correct')
                    count += 1
    else:
        print(f'Congratulations, {name}')
