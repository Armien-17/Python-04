# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruitlist=["apple", "bannana", "kiwi", "watermelon", "strawberry"]
# TODO: Use a for loop to print each fruit in the list
for fruit in fruitlist :
    print(fruit)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count>0:
     print(count)
     count-=1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()
# TODO: Use a for loop to print the first 10 square numbers
for square in range(1,11):
     print(square**2)
#-------------------------------------------------------------------------

# Question 4: Using the random module
# TODO: Import the random module
import random 
# TODO: Create a list of colors
colors = ['red', 'blue', 'black', 'grey', 'pink']
# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    print(random.choice(colors))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
# TODO: Import the custom module and use its functions
import math_operations as matho
print(matho.add(5,17))
print(matho.subtract(8,4))
print(matho.multiply(17,17))
print(matho.divide(17,2))
# TODO: Use a while loop to create a simple calculator
def calculator():
    while True:
        print("Enter '+' to add two numbers")
        print("Enter '-' to sbtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")

operation = input("Enter a function here: ")
number1 = int(input("Enter a number here: "))
number2 = int(input("Enter a number please: "))

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
else:
    print(number1 / number2)
    