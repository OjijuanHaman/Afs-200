def findUpperLowerCases(string):
    numberOfUppercase = 0
    numberOfLowercase = 0
    # Remove white spaces.
    noSpaces = string.replace(" ", "")
    for i in range(0, len(noSpaces)):
        if(noSpaces[i].isupper()):
            numberOfUppercase = numberOfUppercase + 1
        if(noSpaces[i].islower()):
            numberOfLowercase = numberOfLowercase + 1
    print('Your string was:\n', string, '\nWhich has...\n', numberOfUppercase, 'uppercase characters, and..\n', numberOfLowercase, 'lowercase characters.')

userInput = input("Enter string: ")

findUpperLowerCases(userInput)