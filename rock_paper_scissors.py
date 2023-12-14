import random


def get_computer_choice():
    return random.choice(('Rock', 'Paper', 'Scissors'))


def get_user_choice():
    user_choice = input('Enter Rock, Paper or Scissors: ').capitalize()

    while user_choice not in ('Rock', 'Paper', 'Scissors'):
        print('Invalid choice. Please try again.')
        user_choice = input('Enter Rock, Paper or Scissors: ').capitalize()

    return user_choice


def is_win(user_choice, computer_choice):

    global user_score, computer_score

    if user_choice == computer_choice:
        print(f'Both player selected {user_choice}')
    elif user_choice == 'Rock':
        if computer_choice == 'Paper':
            print(f'You win.')
            user_score += 1
        else:
            print(f'You lose.')
            computer_score += 1
    elif user_choice == 'Paper':
        if computer_choice == 'Rock':
            print(f'You win.')
            user_score += 1
        else:
            print(f'You lose.')
            computer_score += 1
    elif user_choice == 'Scissors':
        if computer_choice == 'Paper':
            print(f'You win.')
            user_score += 1
        else:
            print(f'You lose.')
            computer_score += 1


if __name__ == '__main__':

    rounds = int(input("Enter the number of rounds to play: "))
    user_score = 0
    computer_score = 0

    for _ in range(rounds):
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        is_win(user_choice, computer_choice)

    print(f'User score is {user_score}.')
    print(f'Computer score is {computer_score}.')

    if user_score > computer_score:
        print('You win.')
    else:
        print('You lose.')
