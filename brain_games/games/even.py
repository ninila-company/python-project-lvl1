import prompt
import random


def check_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        number_random = random.randint(1, 100)
        print(f'Question: {number_random}')

        def parity_check(number):
            return 'yes' if number % 2 == 0 else 'no'

        answer_one = prompt.string('Your answer: ').lower()
        if answer_one != parity_check(number_random):
            print(f"{answer_one} is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct')
            count += 1

    else:
        print(f'Congratulations, {name}')
