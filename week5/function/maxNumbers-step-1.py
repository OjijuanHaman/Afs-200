#Find the max of 3 numbers
numbers = []

def findMaximum(numbers):
    return max(numbers)

def findMinimum(numbers):
    return min(numbers)

#print(findMaximum(5,3,16))
#Output: 16

for i in range(3):
    userInput = int(input("Enter number: "))
    numbers.append(userInput)

print("The MINIMUM number inputted is:", findMinimum(numbers))
print("The MAXIMUM number inputted is:", findMaximum(numbers))
