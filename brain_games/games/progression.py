import prompt
import random


def arithmetic_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What number is missing in the progression?')

    progressions = {
        'one': '1, 4, 7, 10, 13, 16, 19, 22, 25, 28',
        'two': '2, 4, 6, 8, 10, 12, 14, 16, 18, 20',
        'three': '5, 10, 15, 20, 25, 30, 35, 40, 45, 50',
    }

    def random_elem(lst, number):
        new_lst = lst[:]
        new_lst[number] = '..'
        string = ' '.join(new_lst)
        print(string)
        return string

    for value in progressions.values():
        random_number = random.randint(0, 9)
        list_value = value.split(', ')
        random_elem(list_value, random_number)

        answer = prompt.integer('Your answer: ')
        if answer == int(list_value[random_number]):
            print('Correct')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was '
                  f'"{list_value[random_number]}".')
            print(f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations, {name}')
