from random import randrange

# Take user input for lambda
userInput = input('Enter a number: ')

# Multiply by a random unknown given number in a lambda
randomMultiply = lambda userNumber:int(userNumber)*randrange(1,10) 

# Printing result (userInput * randrange(1,10))
print(randomMultiply(userInput))