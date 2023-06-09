import prompt
import random


def check_divisors(n1, n2):
    divisor = 1
    list_divisors = []
    while divisor <= n1 and divisor <= n2:
        if n1 % divisor == 0 and n2 % divisor == 0:
            list_divisors.append(divisor)
        divisor += 1
    return max(list_divisors)


def greatest_common_factor():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    count = 0
    while count < 3:
        number_one = random.randint(1, 100)
        number_two = random.randint(1, 100)
        print(f'Question: {number_one} {number_two}')

        answer = prompt.integer('Your answer: ')
        if answer != check_divisors(number_one, number_two):
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was '
                  f'{check_divisors(number_one, number_two)}.')
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
            count += 1

    else:
        print(f'Congratulations, {name}!')
