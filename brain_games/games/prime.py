import prompt
import random
import math


def is_prime(number):
    if number == 2:
        return 'yes'
    divisor = 2
    limit = int(math.sqrt(number))
    while divisor <= limit:
        if number % divisor == 0:
            return 'no'
        divisor += 1
    else:
        return 'yes'


def check_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is prime, otherwise answer "no".')

    count = 0
    while count < 3:
        number_random = random.randint(2, 100)
        print(f'Question: {number_random}')

        answer = prompt.string('Your answer: ')
        if answer != is_prime(number_random):
            print(f'"{answer}" is wrong answer ;(.'
                  f'Correct answer was "{is_prime(number_random)}".')
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
            count += 1

    else:
        print(f'Congratulations, {name}!')
