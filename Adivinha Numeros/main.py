# I'm trying to create a guessing number game, it's my first project in python after ending a basic course by Gustavo Guanabara at Curso em Video channel, the following code is the basic created for me and needs to be improved. The idea is to implement a ranking feature to save the players and finnaly a simple GUI.


from random import randint

name = input('Type your name :')
age = input('How old are you :')

try:
    difficulty = int(input(
        f'{name}, choose the difficulty \n[Easy = 1] - [Medium = 2] - [Hard = 3]\n'))
except:
    print('Invalid option, easy level has been chosen automatically')
    difficulty = 1

print(f'{name} guess 1 (one) number between 1 and {10 ** difficulty}, good luck!!')
print(f'Your initial score starts with {10 ** difficulty} points and decreases by half at each wrong guess')

attempts = 0
guessedNumbers = list()
score = 10 ** difficulty
randomized = randint(1, 10 ** difficulty)

while True:
    try:
        guess = int(input('Whats your guess ?'))
        attempts += 1

        if guess > randomized:
            print('go down')
            guess = str(f'\033[1;31m{guess}\033[m')
            guessedNumbers.append(guess)
            score /= 2
        elif guess < randomized:
            print('go up')
            guess = str(f'\033[1;34m{guess}\033[m')
            guessedNumbers.append(guess)
            score /= 2
        else:
            print(f'Good, you win in {attempts} attempts')
            guess = str(f'\033[1;32m{guess}\033[m')
            guessedNumbers.append(guess)
            print('Your chosen numbers were')
            for i in guessedNumbers:

                print(i)
            print()

            print(f'Your score is {score} pts')
            break
    except:
        print("It's wrong, try again")
