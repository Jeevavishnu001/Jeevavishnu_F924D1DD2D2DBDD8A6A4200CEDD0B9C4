def factorial(n):…

# Input from the user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
