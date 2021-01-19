import prompt


def check_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: 15')
    while True:
        answer_one = prompt.string('Your answer: ').lower()
        if answer_one != 'no':
            print(f"{answer_one} is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct')
        print('Question: 6')
        answer_two = prompt.string('Your answer: ').lower()
        if answer_two != 'yes':
            print(f"{answer_two} is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct')
        print('Question: 7')
        answer_three = prompt.string('Your answer: ').lower()
        if answer_three != 'no':
            print(f"{answer_three} is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct')
        print(f'Congratulations, {name}')
        break
