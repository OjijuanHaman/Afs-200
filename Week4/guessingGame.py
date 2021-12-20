import random
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')

def Setup():
    print('Welcome to Number guessing Fun!')
    name = input('Type your name: ')
    print(name, 'is a cool name! Now, lets play..')
    range = int(input('Enter a starting number for a range for your game: '))
    range2 = int(input('Enter in the last number your number could be: '))

    # Guesses counter, getting a random number for this game.
    guesses = 0
    previouslyGuessedNumbers = []
    numberToGuess = random.randint(range, range2)
    currentGuess = ''
    exit = False

    clear()
    print('Alright! We are ready to give you an attempt at this number. \nSee how few times you can guess before you get it right! \nWe will keep count for you. \nThe Range is:', range, 'to', range2)
    Game(currentGuess, guesses, numberToGuess, exit, name, previouslyGuessedNumbers)

def Game(currentGuess, guesses, numberToGuess, exit, name, previouslyGuessedNumbers):
    while currentGuess != numberToGuess:
        currentGuess = input('Enter your guess: ')
        clear()

        if currentGuess == 'exit':
            # This will create a false win without a message to exit the loop. The player wishes to exit the game.
            currentGuess = numberToGuess
            print('The number was:', numberToGuess)
            print('You have chosen to exit, exiting the game..')
            exit = True
        else:
            # Check if the string contains a number, isdigit is a method of a string, if 1 guess has been made, it will need to be converted back because int has no attribute of 'isdigit'
            currentGuess = str(currentGuess)
            if currentGuess.isdigit() == False:
                print('Please only use numbers. If you\'re trying to quit, try \'exit\' instead.')
            else:
                # If the case is not to exit, convert the input into a number to compare against integers
                currentGuess = int(currentGuess)

                if currentGuess in previouslyGuessedNumbers:
                    print('You have already guessed this number!')
                    guesses += 1

                if currentGuess > numberToGuess:
                    print('Your guess is too high! (try a smaller number)')
                    guesses += 1
                    previouslyGuessedNumbers.append(currentGuess)

                if currentGuess < numberToGuess:
                    print('Your guess is too low! (try a bigger number)')
                    guesses += 1
                    previouslyGuessedNumbers.append(currentGuess)

                if currentGuess == numberToGuess:
                    print('You\'ve guessed the number! It was', numberToGuess)
                    guesses += 1

    # They will only hit below the while loop while exiting or have guessed correctly. Displaying statistics for the game.
    print('Hope you had fun,', name, '!\nYou guessed:', guesses, 'times!')
    if exit == False:
        Setup()

Setup()